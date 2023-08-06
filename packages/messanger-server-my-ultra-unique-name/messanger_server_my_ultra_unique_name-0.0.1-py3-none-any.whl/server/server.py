import logging
import socket
import sys
import time
import traceback

import select
import threading

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from config.variables import DEFAULT_PORT, DEFAULT_IP_ADDRESS, MAX_PACKAGE_LENGTH, ENCODING
from config.utils import get_message, send_message
from descriptors import Port
from metaclasses import ServerVerifier
from server_libs.server_database import create_session, User, UserHistory, ActiveUser
from server_libs.server_gui import MainWindow, gui_create_model, HistoryWindow, create_stat_model

logger = logging.getLogger('server_logger')


class Server(threading.Thread, metaclass=ServerVerifier):
    port = Port()

    def __init__(self, addr, port):

        self.addr = addr
        self.port = port
        self.client_list = []
        self.message_list = []
        # имя пользователя: его сокет
        self.users_dict = {}

        self.sock = None
        super().__init__()

    def init_socket(self):
        """
        Инициализация сокета
        :return:
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.addr, self.port))
        server.settimeout(0.5)

        self.sock = server
        self.sock.listen()
        logger.info(f'Запущен сервер по адресу {server.getsockname()}')

    def process_client_message(self, message, client):
        """
        Читает словарь от клиента и формирует ответ в виде словаря
        """
        logger.info(message)
        logger.debug('Читается словарь от клиента')
        if 'action' in message:
            session = create_session()
            # если сообщение о присутствии
            if message['action'] == 'presence' and 'time' in message and 'user' in message:
                # если такого имени юзера ещё нет, то регистрируем, если есть - отправляем ответ
                if message['user']['account_name'] not in self.users_dict.keys():
                    logger.info(f"На сервере новый пользователь - {message['user']['account_name']}")
                    self.users_dict[message['user']['account_name']] = client
                    client_ip, client_port = client.getpeername()
                    User.login_user(session, message['user']['account_name'], client_ip, client_port)
                    send_message(client, {'response': 200}, ENCODING)
                else:
                    response = {
                        'response': 400,
                        'error': 'Имя пользователя уже занято.'
                    }
                    send_message(client, response)
                    self.client_list.remove(client)
                    client.close()
                session.close()
                return
            # если отправка сообщения пользователем
            elif message['action'] == 'message' \
                    and 'time' in message and 'sender' in message and 'message_text' and 'destination' in message:
                self.message_list.append(message)
                # добавляем в историю отправленных и полученных сообщений
                sender = session.query(User).filter(User.name == message['sender']).first()
                dest = session.query(User).filter(User.name == message['destination']).first()
                history_sender = session.query(UserHistory).filter(UserHistory.user == sender).first()
                history_sender.sent += 1
                history_dest = session.query(UserHistory).filter(UserHistory.user == dest).first()
                history_dest.accepted += 1
                session.commit()
                session.close()
                return
            # если клиент отключается
            elif message['action'] == 'exit' and 'account_name' in message:
                logger.info(f'Пользователь {message["account_name"]} отключается')
                User.logout_user(session, message["account_name"])
                self.client_list.remove(self.users_dict[message['account_name']])
                self.users_dict[message['account_name']].close()
                del self.users_dict[message['account_name']]
                session.close()
                return
            elif message['action'] == 'get_contacts' and 'time' in message and 'user_login' in message:
                logger.debug(f'Пользователь {message["user_login"]} запрашивает список юзеров')
                user_list = [i[0] for i in session.query(User.name).all()]
                response = {
                    'response': 200,
                    'alert': user_list
                }
                send_message(client, response)
                session.close()
                return
            elif message['action'] == 'auth':
                logger.debug(f'Пользователь {message["user"]["account_name"]} запрашивает авторизацию')
                user = session.query(User).filter(User.name == message["user"]["account_name"]).first()
                if user and str(user.password) == message["user"]["password"]:
                    send_message(client, {'response': 200, 'message': 'auth success'})
                else:
                    send_message(client, {'response': 401, 'message': 'auth fail'})
                session.close()
        else:
            send_message(client, {
                'response': 400,
                'error': 'Bad Request'
            }, ENCODING)
            return

    def process_message(self, message, listen_socks):
        """
        Отправляет сообщение конкретному юзеру
        """
        if message['destination'] in self.users_dict and self.users_dict[message['destination']] in listen_socks:
            if self.users_dict[message['destination']] in listen_socks:
                send_message(self.users_dict[message['destination']], message)
                logger.info(f'Отправлено сообщение пользователю {message["destination"]} '
                            f'от пользователя {message["sender"]}')
            else:
                raise ConnectionError
        else:
            logger.error(
                f'Пользователь {message["destination"]} не зарегистрирован на сервере, '
                f'отправка сообщения невозможна')

    def run(self):
        self.init_socket()

        while 1:
            try:
                client, client_address = self.sock.accept()
            except Exception:
                pass
            else:
                logger.info(f'Установлено соединение с клиентом {client_address}')
                self.client_list.append(client)
            recv_data_lst = []
            send_data_lst = []
            try:
                if self.client_list:
                    recv_data_lst, send_data_lst, err_lst = select.select(self.client_list, self.client_list, [], 0)
            except Exception:
                pass
            if recv_data_lst:
                for client in recv_data_lst:
                    try:
                        self.process_client_message(get_message(client, MAX_PACKAGE_LENGTH, ENCODING), client)
                    except Exception:
                        session = create_session()
                        session.query(ActiveUser).filter(ActiveUser.ip_address == client.getpeername()[0],
                                                         ActiveUser.port == client.getpeername()[1]).delete()
                        session.commit()
                        session.close()
                        logger.info(traceback.format_exc())
                        logger.info(f'Клиент {client.getpeername()} отключился от сервера.')
                        if client in self.client_list:
                            self.client_list.remove(client)

            for message in self.message_list:
                try:
                    self.process_message(message, send_data_lst)
                except Exception:
                    logger.info(f'Связь с клиентом с именем {message["destination"]} была потеряна')
                    self.client_list.remove(self.users_dict[message['destination']])
                    del self.users_dict[message['destination']]
            self.message_list.clear()


if __name__ == '__main__':
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        logger.error('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        logger.error('Порт должен быть в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = DEFAULT_IP_ADDRESS
    except IndexError:
        logger.error('После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    server = Server(listen_address, listen_port)
    server.daemon = True
    server.start()

    #  создаём графический интерфейс
    server_app = QApplication(sys.argv)
    main_window = MainWindow()

    # изменяем данные в окне
    main_window.statusBar().showMessage('Server Working')


    # обновляем активных юзеров
    def active_users_update():
        main_window.active_clients_table.setModel(gui_create_model())
        main_window.active_clients_table.resizeColumnsToContents()
        main_window.active_clients_table.resizeRowsToContents()


    # показывает статистику по клиентам
    def show_statistics():
        stat_window = HistoryWindow()
        stat_window.history_table.setModel(create_stat_model())
        stat_window.history_table.resizeColumnsToContents()
        stat_window.history_table.resizeRowsToContents()
        stat_window.exec_()


    # заполняем первично активных юзеров
    active_users_update()

    # Таймер, обновляющий список клиентов 1 раз в секунду
    timer = QTimer()
    timer.timeout.connect(active_users_update)
    timer.start(1000)

    # Связываем кнопки с процедурами
    main_window.refresh_button.triggered.connect(active_users_update)
    main_window.show_history_button.triggered.connect(show_statistics)

    # запускаем графический интерфейс
    server_app.exec_()
