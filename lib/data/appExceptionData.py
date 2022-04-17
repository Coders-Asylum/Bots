from enum import Enum
from colorama import Fore
import logging as log

from ..handlers.response_handler import Response


class ExceptionType(Enum):
    CLOSE = Fore.RED + '[!] Program execution stopped due to a fatal error.'
    WARNING = Fore.YELLOW + '[W] '


class AppException(Exception):
    """ Exception class to handle various exception raised during app runtime.
    """

    def __int__(self, **kwargs):
        super().__init__(self, kwargs['msg'])
        self.__response = kwargs['response']

    @staticmethod
    def log(msg):
        """ Logs exception message into logger.

        Args:
            msg: exception message that has to be logged

        Returns: None

        """
        log.exception(msg=Fore.RED + msg, stack_info=True)

    @property
    def response(self):
        """

        Returns (Response): Response object for the current exception.

        """
        return self.__response


class GithubAppApiException(AppException):

    def __int__(self, msg: str, api: str, response: Response):
        super(GithubAppApiException, self).__int__(msg=msg, response=response)
        super().log(msg=f'{msg} \n Response data from App {api} api: \n\t {response.status_code} {response.status} \n\t{response.data}')


class GithubApiException(AppException):

    def __int__(self, msg: str, api: str, response: Response):
        _msg = f''
        super(GithubApiException, self).__int__(msg=msg, response=response)
