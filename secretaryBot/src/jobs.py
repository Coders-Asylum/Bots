from azure import functions as func


class jobs:
    _req: func.HttpRequest

    def __init__(self, req: func.HttpRequest):
        self._req = req

    def map_request(self):
        pass
