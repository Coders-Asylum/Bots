# from lib.handlers import Exception_Handler
# from lib.data import ExceptionType
# from lib import install_package
#
#
# class initialise:
#     exec_handler = Exception_Handler()
#
#     def check_requests_package(self):
#         try:
#             import requests
#         except ImportError as err:
#             print(f"[E] Error while initialising: {err.name}- {err.msg}")
#             print("[I] Trying to import package...")
#             check = install_package(requests)
#             if check is 0:
#                 pass
#             else:
#                 self.exec_handler.handle(exception_type=ExceptionType.CLOSE, message='[E] Unable to install package: '
#                                                                                      'requests')
#
#     def check_git(self):
#         pass
