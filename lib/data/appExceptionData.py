from enum import Enum
from colorama import Fore
import logging as log

from . import Message
from ..handlers.response_handler import Response


class ExceptionType(Enum):
    CLOSE = Fore.RED + 'Program execution stopped due to a fatal error.'
    WARNING = Fore.YELLOW
    ERROR = Fore.RED


class AppException(Exception):
    """ Exception class to handle various exception raised during app runtime.
    """

    __msg: Message = Message()

    def __init__(self, **kwargs):
        self.__response: Response = kwargs['response']
        self.__error_type: ExceptionType = kwargs['error_type']
        self.__api = kwargs['api']
        self.log(kwargs['msg'])
        super().__init__(self, kwargs['msg'])

    def log(self, msg):
        """ Logs exception message into logger.

        **Note: all logging is done under `root`.**

        Args:
            msg: exception message that has to be logged

        Returns: None

        """
        if self.__error_type is ExceptionType.ERROR:
            log.exception(self.__error_type.value + msg + f'\n{self.__msg.seperator}\n' + Fore.MAGENTA, stack_info=True)
        elif self.__error_type is ExceptionType.WARNING:
            log.warning(self.__error_type.value + msg + f'\n{self.__msg.seperator}\n' + Fore.MAGENTA, stack_info=True)
        elif self.__error_type is ExceptionType.CLOSE:
            log.critical(self.__error_type.value + f'\n Reason: {msg}' + f'\n{self.__msg.seperator}\n' + Fore.MAGENTA, stack_info=True)
        else:
            log.warning(ExceptionType.WARNING.value + f' {msg}' + f'\n{self.__msg.seperator}\n')

    @property
    def response(self):
        """ Response data during exception

        Returns (Response): Response object for the current exception.

        """
        return self.__response

    @property
    def api(self):
        """ Api from which exception was raised

        Returns (str): Name of the API.

        """
        return self.__api


class GithubAppApiException(AppException):

    def __init__(self, msg: str, api: str, response: Response, error_type: ExceptionType = ExceptionType.WARNING):
        __msg = f'{msg} \n Response data from App {api} api: \n\t {response.status_code} {response.status} \n\t{response.data}'
        super().__init__(msg=__msg, error_type=error_type, response=response, api=api)


class GithubApiException(AppException):

    def __init__(self, msg: str, api: str, response: Response, error_type: ExceptionType = ExceptionType.WARNING):
        __msg = f'{msg} \n Response data from {api} api: \n\t {response.status_code} {response.status} \n\t{response.data}'
        super().__init__(msg=__msg, error_type=error_type, response=response, api=api)
