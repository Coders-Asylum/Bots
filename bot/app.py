from logging import info
from datetime import datetime
from azure.functions import HttpRequest, HttpResponse
from json import dumps
from lib.handlers import Response
from .src import Jobs
from lib.data import Message, Webhook


class App:
    _req: HttpRequest
    _res: Response
    _job: Jobs

    _dump: str = dumps({'message': 'Unknown Error'})

    def __init__(self):
        self._job = Jobs()
        self._res = Response(status_code=400, status='Bad Request', data=self._dump)
        info(f'[I] App session started on {datetime.utcnow()}')

    def __del__(self):
        info(f'[I] App session ended on {datetime.utcnow()}')

    def execute(self, req: HttpRequest) -> HttpResponse:
        try:
            req_body = req.get_json()
        except ValueError:
            self._res = Response(status_code=400, status='Bad Request', data=Message.http_body_incorrect)
            return self._res.disintegrated()

        try:
            webhook = Webhook(req_body)
        except KeyError:
            if req_body == {} or req_body == []:
                self._res = Response(status_code=422, status='Unprocessable Entity', data=Message.http_body_empty)
            else:
                self._res = Response(status_code=422, status='Unprocessable Entity', data=Message.http_body_semantic_error)
            return self._res.disintegrated()

        if webhook.type == 'published':
            if webhook.data['repository']['name'] == 'coders-asylum.github.io':
                self._res = self._job.push_new_blog_page()
            else:
                self._res = Response(status_code=202, status='Accepted', data=Message.no_processing_required)

        else:
            self._res = Response(status_code=202, status='Accepted', data=Message.no_processing_required)

        return self._res.disintegrated()


if __name__ == '__main__':
    print('Running main')
