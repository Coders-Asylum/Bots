from subprocess import run
from requests import get, structures, post, patch
from azure.functions import HttpResponse


class Response:
    status_code: int = None
    status: str = None

    data: str = None
    _response: HttpResponse = None

    def __init__(self, status_code: int, status: str, data: str):
        self.status_code = status_code
        self.data = data
        self.status = status
        self._response = HttpResponse(status_code=status_code, body=data)

    def disintegrated(self) -> HttpResponse:
        """HttpResponse made by striping data from current object

        Returns: HttpResponse object

        """
        return self._response


# todo: create function to extract data and for_status from response


class ResponseHandlers:
    def __init__(self):
        pass

    _r = None

    @staticmethod
    def curl_get_response(url: str, headers: structures.CaseInsensitiveDict):
        _r = get(url=url, headers=headers)
        return Response(status_code=_r.status_code, data=_r.text, status=_r.reason)

    @staticmethod
    def curl_post_response(url: str, headers: structures.CaseInsensitiveDict, data: str):
        """
        cURL put function to the given url, headers and data
        :param url: Url to post
        :param headers: headers data as CaseInsensitiveDict
        :param data: data to be posted to the url
        :return:
        """
        _r = post(url=url, headers=headers, data=data)
        return Response(status_code=_r.status_code, data=_r.text, status=_r.reason)

    @staticmethod
    def http_patch(url: str, headers: structures.CaseInsensitiveDict, data: str) -> Response:
        """ Patch request to the given url with the headers and data specified.

        Args:
            url (str): url to which the request has to be made
            headers (str): Header data that needs to be sent with the request.
            data (str): data in str format that has to be patched to the server.

        Returns:
            A Response object with the response after the attempt to do a Http patch.
        """
        _r = patch(url=url, headers=headers, data=data)
        return Response(status_code=_r.status_code, data=_r.text, status=_r.reason)

    @staticmethod
    def http_get_response(url: str):
        """
        Gets Http response using requests module and returns data
        This function does not pass any header data, it performs a simple get request to the specified `url`
        :param url: url for which get request has to be made
        :return: Response
        """
        _http_get = get(url)

        if _http_get.status_code == 200:
            return Response(status_code=_http_get.status_code, data=_http_get.text, status=_http_get.reason)
        else:
            return Response(status_code=_http_get.status_code, data='No Data', status=_http_get.reason)

    @staticmethod
    def shell_response(command, output=False):
        if output is False:
            _c = run(command)
            if _c.returncode == 0:
                return Response(_c.returncode, 'ok', 'None')
            else:
                return Response(_c.returncode, 'error', 'None')
        else:
            _c = run(command, capture_output=True)
            if _c.returncode == 0:
                return Response(_c.returncode, 'ok', str(_c))
            else:
                return Response(_c.returncode, 'error', str(_c))

    # @staticmethod
    # def function_response(response: Response) -> func.HttpResponse:
    #     """
    #     Returns a process response in Azure Function Http Response type
    #     :param Response response: the response object that needs to be converted
    #     :return --> func.HttpResponse
    #     """
    #     return func.HttpResponse(status_code=response.status_code, body=response.data)
