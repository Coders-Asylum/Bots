from bin.handlers.response_handler import ResponseHandlers, Response
from shlex import split


def install_package(package):
    args = split('pip3 install {} --retries'.format(package))
    _r = ResponseHandlers.shell_response(command=args, output=False)
    return Response.status_code
