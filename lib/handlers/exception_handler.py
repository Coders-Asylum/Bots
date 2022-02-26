from enum import Enum
import logging as log
from sys import exit
from colorama import Fore


class ExceptionType(Enum):
    CLOSE = Fore.RED + '[!] Program execution stopped due to a fatal error.'


class Exception_Handler:

    def __init__(self):
        pass

    @staticmethod
    def _exit_execution():
        exit()

    # todo: add flag to send email, if flag is set to true to group of users, email code should be added to utils.py
    def handle(self, exception_type, message):
        print(Fore.BLUE + '[I] ' + message)
        if exception_type is ExceptionType.CLOSE:
            log.exception(f'[E] {message}')
            log.info(f'[I] {exception_type.value}')
            self._exit_execution()


if __name__ == '__main__':
    exe = Exception_Handler()
    exe.handle(ExceptionType.CLOSE, 'Log')
