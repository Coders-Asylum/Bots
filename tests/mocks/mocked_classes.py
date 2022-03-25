from re import match
from tests.mocks.github_api_mocks import GithubAPIMock, Status
from lib import Response


class MockedResponseHandlers:
    commit_url = r'^https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/commits\/\w+'
    tree_url = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/trees\/\w+'
    ref_url = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/ref\/heads\/\w+'
    file_url = r'https:\/\/raw.githubusercontent.com\/Coders-Asylum\/fuzzy-train\/test_branch\/\w+\/\w+\/\w+.\w+'
    blob_post_url = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/blobs'
    gapi_success = GithubAPIMock(for_status=Status.SUCCESS)

    def mocked_http_get_response(self, *args, **kwargs) -> Response:
        if args is None or len(args) == 0:
            url = kwargs['url']
        else:
            url = args[0]

        if bool(match(self.commit_url, url)):
            return self.gapi_success.get_commit()
        elif bool(match(self.tree_url, url)):
            return self.gapi_success.get_tree()
        elif bool(match(self.ref_url, url)):
            return self.gapi_success.getref()
        elif bool(match(self.file_url, url)):
            return self.gapi_success.download_repo_file()
        else:
            return self.gapi_success.response

    def mocked_http_post_response(self, *args, **kwargs):
        if args is None or len(args) == 0:
            url = kwargs['url']
        else:
            url = args[0]

        if bool(match(self.blob_post_url, url)):
            return self.gapi_success.post_blob()
        else:
            return self.gapi_success.response
