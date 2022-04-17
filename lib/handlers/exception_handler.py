import logging as log
from sys import exit
from logging import log

from lib.data import ExceptionType


class Exception_Handler:

    def __init__(self):
        pass

    @staticmethod
    def _exit_execution():
        exit()

    # todo: add flag to send email, if flag is set to true to group of users, email code should be added to utils.py
    def handle(self, exception_type, message):
        if exception_type is ExceptionType.CLOSE:
            log.exception(f'[E] {message}')
            log.info(f'[I] {exception_type.value}')
            self._exit_execution()
        elif exception_type is ExceptionType.WARNING:
            print(f'{exception_type.value} {message}')


if __name__ == '__main__':
    exe = Exception_Handler()
    exe.handle(ExceptionType.WARNING, 'Log')
