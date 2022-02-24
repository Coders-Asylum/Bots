import azure.functions as func


class app:
    _req: func.HttpRequest
    _res: func.HttpResponse

    def __init__(self, req: func.HttpRequest):
        self._req = req

    def map_requests(self):
        pass

    def execute(self) -> func.HttpResponse:
        return self._res


if __name__ == '__main__':
    print('Running main')
