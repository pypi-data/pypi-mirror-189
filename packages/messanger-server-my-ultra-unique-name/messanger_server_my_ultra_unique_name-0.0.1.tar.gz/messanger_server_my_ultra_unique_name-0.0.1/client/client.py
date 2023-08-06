import json
import logging
import sys
import socket
import threading
import time
import traceback

from datetime import datetime
from sqlalchemy import or_
from PyQt5.QtWidgets import QApplication

import logs.config.client_log_config

from config.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, ENCODING, MAX_PACKAGE_LENGTH
from config.utils import get_message, send_message
from metaclasses import ClientVerifier
from client_database import create_session, Contact, MessageHistory
from client_libs.start_dialog import UserNameDialog
from client_libs.main_window import ClientMainWindow
from client_libs.transport import ClientTransport

logger = logging.getLogger('client_logger')


def main():
    """
    Функция запуска клиентской стороны. В командной строке запустить: py client.py <host> <int:port>.
    """
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            logger.error('Порт должен быть в диапазоне от 1024 до 65535.')
            raise ValueError
    except IndexError:
        logger.debug('Применяются дефолтные настройки хоста и порта')
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        sys.exit(1)

    # основное приложение
    client_app = QApplication(sys.argv)
    # запрашиваем имя юзера
    start_dialog = UserNameDialog()
    client_app.exec_()
    if start_dialog.ok_pressed:
        client_name = start_dialog.client_name.text()
        client_passwd = start_dialog.client_passwd.text()
        del start_dialog
    else:
        sys.exit(-1)

    try:
        logger.debug('Инициализирую объект клиента')
        transport = ClientTransport(server_port, server_address, client_name, client_passwd)
    except Exception as e:
        logger.critical(traceback.format_exc())
        sys.exit(-1)
    else:
        logger.debug('Запускаю клиента')
        transport.daemon = True
        transport.start()

    main_window = ClientMainWindow(transport, client_name)
    main_window.make_connection(transport)
    main_window.setWindowTitle(f'Клиент {client_name}')
    client_app.exec_()

    transport.transport_shutdown()
    transport.join()


if __name__ == '__main__':
    main()
