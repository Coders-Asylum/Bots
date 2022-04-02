from azure.functions import HttpRequest, HttpResponse
from json import dumps
from lib.data import Webhook
from lib.handlers import Response
from src import Jobs


class App:
    _req: HttpRequest
    _res: Response
    _job:Jobs

    _dump:str = dumps({'message':'No processing needed'})

    def __init__(self, req: HttpRequest):
        self._req = req
        self._job = Jobs()
        self._res = Response(status_code=202, status='Accepted', data=self._dump)

    def execute(self) -> HttpResponse:
        webhook: Webhook = Webhook(self._req)
        if webhook.type == 'published':
            if webhook.data['repository']['name'] == 'coders-asylum.github.io':
                self._job.push_new_blog_page()

        return self._res.disintegrated()


if __name__ == '__main__':
    print('Running main')
