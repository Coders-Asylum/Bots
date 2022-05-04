from logging import Formatter, DEBUG, INFO, WARNING, CRITICAL, ERROR
from lib.handlers import ResponseHandlers, Response
from shlex import split


# def install_package(package):
#     args = split('pip3 install {} --retries'.format(package))
#     _r = ResponseHandlers.shell_response(command=args, output=False)
#     return Response.status_code


class ColoredShellFormatter(Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    magenta = "\x1b[0;35m"
    reset = "\x1b[0m"

    __format: str = "%(asctime)s:[%(name)s][%(levelname)s]:%(message)s (%(filename)s:%(lineno)d)"
    __format_debug: str = "%(asctime)s:[%(name)s][%(levelname)s]:%(message)s (%(filename)s:%(lineno)d): [%(threadName)s- %(thread)d] [%(process)d]"

    FORMATS = {
        DEBUG: grey + __format_debug + reset,
        INFO: grey + __format + reset,
        WARNING: yellow + __format + reset,
        ERROR: red + __format + reset,
        CRITICAL: bold_red + __format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = Formatter(log_fmt)
        return formatter.format(record)
