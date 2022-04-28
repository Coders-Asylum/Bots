from sys import exit

from lib.data import ExceptionType, BotConfig
from lib.data.appExceptionData import AppException
from lib.handlers import GithubAPIHandler


class Exception_Handler:
    __config: BotConfig = BotConfig()
    __g_api: GithubAPIHandler = GithubAPIHandler(owner=__config.repo_owner, repo=__config.repo_name, branch='master')
    __exception: AppException

    def __init__(self, exception: AppException = None):
        self.__exception = exception

    @staticmethod
    def _exit_execution():
        exit()

    # todo: add flag to send email, if flag is set to true to group of users, email code should be added to utils.py
    def handle(self, exception_type, message):
        if exception_type is ExceptionType.CLOSE:
            self._exit_execution()
        elif exception_type is ExceptionType.WARNING:
            print(f'{exception_type.value} {message}')
        elif exception_type is ExceptionType.ERROR:
            __body: str = f'{self.__exception.response.data}'
            self.__g_api.create_issue(title=f'[Runtime Issue] Issue in {self.__exception.api}', body=__body, labels=['bug'])


if __name__ == '__main__':
    exe = Exception_Handler()
    exe.handle(ExceptionType.WARNING, 'Log')
