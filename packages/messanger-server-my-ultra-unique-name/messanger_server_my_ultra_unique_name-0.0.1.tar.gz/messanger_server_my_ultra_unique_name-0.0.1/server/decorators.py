import logging
import sys
import inspect

import logs.config.client_log_config
import logs.config.server_log_config

if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server_logger')
else:
    logger = logging.getLogger('client_logger')


def log(func):
    """
    Логирование вызова функции
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug(f'Функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}',
                     stacklevel=2)
        return res

    return wrapper
