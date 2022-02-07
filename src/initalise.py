import argparse
import subprocess
from bin.handlers.exception_handler import Exception_Handler, ExceptionType

from bin.utils import install_package


class initialise:
    exec_handler = Exception_Handler()

    def check_requests_package(self):
        try:
            import requests
        except ImportError as err:
            check = install_package(requests)
            if check is 0:
                pass
            else:
                self.exec_handler.handle(exception_type=ExceptionType.CLOSE, message='[E] Unable to install package: '
                                                                                     'requests')

    def check_git(self):
        pass
