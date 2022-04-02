# __init__.py
"""
This is the Aatmaram Bhide Secretary Bot.
"""
from .app import App
from azure.functions import HttpRequest, HttpResponse


def main(req: HttpRequest) -> HttpResponse:
    _app: App = App()
    return _app.execute(req=req)
 