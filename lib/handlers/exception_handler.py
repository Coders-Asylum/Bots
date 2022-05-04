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
    def __exit_execution():
        exit()

    def handle(self, exception_type, message):
        if exception_type is ExceptionType.CLOSE:
            self.__exit_execution()
        elif exception_type is ExceptionType.WARNING:
            print(f'{exception_type.value} {message}')
        elif exception_type is ExceptionType.ERROR:
            __body: str = f'App function stopped due to malfunction of `{self.__exception.api}`.\n ## Response: \nStatus: `{self.__exception.response.status_code} {self.__exception.response.status}` ``` json\n{self.__exception.response.data}\n``` <details>\n<summary>Logs</summary>\n{self.__exception.log_output}\n</details> '
            self.__g_api.create_issue(title=f'[BUG] Issue in {self.__exception.api}', body=__body, labels=['bug'], milestone='P1')


if __name__ == '__main__':
    exe = Exception_Handler()
    exe.handle(ExceptionType.WARNING, 'Log')
