from re import match

from requests.structures import CaseInsensitiveDict

from lib.data import *
from lib.handlers import GithubAccessToken, Response
from tests.mocks.github_api_mocks import GithubAPIMock, Status
from json import dumps, loads


def mocked_token() -> GithubAccessToken:
    data = {"token": "ghs_BWpGokQJ7kJe4vWWir7xLgN6ciyA7e0fDka8",
            "expires_at": "2022-03-29T17:50:04Z",
            "permissions": {"members": "read", "actions": "write", "contents": "write", "issues": "write", "metadata": "read", "pull_requests": "write", "repository_hooks": "read", "workflows": "write"},
            "repository_selection": "selected",
            "repositories": [
                {"id": 457481007,
                 "node_id": "R_kgDOG0SbLw",
                 "name": "fuzzy-train",
                 "full_name": "Coders-Asylum/fuzzy-train",
                 "private": False,
                 "owner": {
                     "login": "Coders-Asylum",
                     "id": 58622402,
                     "node_id": "MDEyOk9yZ2FuaXphdGlvbjU4NjIyNDAy",
                     "avatar_url": "https://avatars.githubusercontent.com/u/58622402?v=4",
                     "gravatar_id": "",
                     "url": "https://api.github.com/users/Coders-Asylum",
                     "html_url": "https://github.com/Coders-Asylum",
                     "followers_url": "https://api.github.com/users/Coders-Asylum/followers",
                     "following_url": "https://api.github.com/users/Coders-Asylum/following{/other_user}", "gists_url": "https://api.github.com/users/Coders-Asylum/gists{/gist_id}",
                     "starred_url": "https://api.github.com/users/Coders-Asylum/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/Coders-Asylum/subscriptions",
                     "organizations_url": "https://api.github.com/users/Coders-Asylum/orgs", "repos_url": "https://api.github.com/users/Coders-Asylum/repos", "events_url": "https://api.github.com/users/Coders-Asylum/events{/privacy}",
                     "received_events_url": "https://api.github.com/users/Coders-Asylum/received_events", "type": "Organization", "site_admin": False}, "html_url": "https://github.com/Coders-Asylum/fuzzy-train",
                 "description": "Sandbox environment for testing integrations and apps", "fork": False, "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train", "forks_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/forks",
                 "keys_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/keys{/key_id}", "collaborators_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/collaborators{/collaborator}"}
            ]
            }
    return GithubAccessToken(data=dumps(data))


class MockedResponseHandlers:
    """ Returns mocked responses for testing Github rest(http) api.
    """
    # commit files urls
    git_commit_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/commits\/c30dbe34699b8e7e522885bc9d2a4d9d141c9382'
    git_post_tree_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/trees'
    git_ref_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/refs\/heads\/test_branch'
    git_post_commit_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/commits'
    git_tree_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/trees\/47b01c17a28529cd72f150f403022fc46d061452'

    file_url: str = r'https:\/\/raw.githubusercontent.com\/Coders-Asylum\/fuzzy-train\/test_branch\/\w+\/\w+\/\w+.\w+'
    blob_post_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/git\/blobs'
    latest_release_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/releases\/latest'
    release_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/releases'
    workflow_trigger_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/actions\/workflows\/\w+.yml\/dispatches'
    tag_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/tags'
    commit_url: str = r'https:\/\/api.github.com\/repos\/Coders-Asylum\/fuzzy-train\/commits\/10f68682850d598a90ed6f5ea237f5b140a5f4f3'

    gapi_success = GithubAPIMock(for_status=Status.SUCCESS)
    gapi_unauthorized = GithubAPIMock(for_status=Status.UNAUTHORIZED)
    gapi_res_not_found = GithubAPIMock(for_status=Status.RES_NOT_FOUND)

    def mocked_http_get_response(self, *args, **kwargs) -> Response:
        """ Mocked responses for HTTP get request

        - Fist args should be url or kwargs "url" and pass the api url.
        - Second args should be for_status or kwargs "for_status" and pass Status.xxx

        Args:
            *args: list arguments
            **kwargs: keyword arguments

        Returns: HTTP api response as a Response object

        """
        if args is None or len(args) == 0:
            url = kwargs['url']
        else:
            url = args[0]

        if bool(match(self.git_commit_url, url)):
            return self.gapi_success.get_git_commit()
        elif bool(match(self.git_tree_url, url)):
            return self.gapi_success.get_git_tree()
        elif bool(match(self.git_ref_url, url)):
            return self.gapi_success.get_latest_ref()
        elif bool(match(self.file_url, url)):
            return self.gapi_success.download_repo_file()
        elif bool(match(self.latest_release_url, url)):
            return self.gapi_success.get_latest_release()
        elif bool(match(self.release_url, url)):
            return self.gapi_success.get_latest_release(latest=False)
        elif bool(match(self.tag_url, url)):
            return self.gapi_success.get_tag()
        elif bool(match(self.commit_url, url)):
            return self.gapi_success.get_commit()
        else:
            return self.gapi_success.response

    def mocked_http_get_res_found_response(self, *args, **kwargs) -> Response:
        """ Mocked responses for HTTP get request with 404 error code

        Args:
            *args: list arguments
            **kwargs: keyword arguments

        Returns: HTTP api response as a Response object

        """
        if args is None or len(args) == 0:
            url = kwargs['url']
        else:
            url = args[0]

        if bool(match(self.git_commit_url, url)):
            return self.gapi_res_not_found.get_git_commit()
        elif bool(match(self.git_tree_url, url)):
            return self.gapi_res_not_found.get_git_tree()
        elif bool(match(self.git_ref_url, url)):
            return self.gapi_res_not_found.get_latest_ref()
        elif bool(match(self.file_url, url)):
            return self.gapi_res_not_found.get_raw_data()
        elif bool(match(self.latest_release_url, url)):
            return self.gapi_res_not_found.get_latest_release()
        elif bool(match(self.release_url, url)):
            return self.gapi_res_not_found.get_latest_release(latest=False)
        elif bool(match(self.tag_url, url)):
            return self.gapi_res_not_found.get_tag()
        elif bool(match(self.commit_url, url)):
            return self.gapi_res_not_found.get_commit()
        else:
            return self.gapi_res_not_found.response

    def mocked_http_post_response(self, *args, **kwargs):
        """ Mocked responses for HTTP post request.

                Args:
                    *args: list arguments
                    **kwargs: keyword arguments

                Returns: HTTP api response as a Response object

                """
        url: str
        data: str
        headers: CaseInsensitiveDict

        if args is None or len(args) == 0:
            url = kwargs['url']
            data = kwargs['data']
            headers = kwargs['headers']
        else:
            url = args[0]
            headers = args[1]
            data = args[2]

        if bool(match(self.blob_post_url, url)):
            return self.gapi_success.post_blob()
        elif bool(match(self.workflow_trigger_url, url)):
            return self.gapi_success.trigger_workflow()
        elif bool(match(self.git_post_tree_url, url)):
            return self.gapi_success.post_git_tree()
        elif bool(match(self.git_post_commit_url, url)):
            return self.gapi_success.post_git_commit()
        else:
            return self.gapi_success.response

    def mocked_http_post_res_not_response(self, *args, **kwargs):
        """ Mocked responses for HTTP post request with 404 error code

               Args:
                   *args: list arguments
                   **kwargs: keyword arguments

               Returns: HTTP api response as a Response object
        """
        url: str
        data: str
        headers: CaseInsensitiveDict

        if args is None or len(args) == 0:
            url = kwargs['url']
            data = kwargs['data']
            headers = kwargs['headers']
        else:
            url = args[0]
            headers = args[1]
            data = args[2]

        if bool(match(self.blob_post_url, url)):
            return self.gapi_res_not_found.post_blob()
        elif bool(match(self.workflow_trigger_url, url)):
            return self.gapi_res_not_found.trigger_workflow()
        elif bool(match(self.git_post_tree_url, url)):
            return self.gapi_res_not_found.post_git_tree()
        elif bool(match(self.git_post_commit_url, url)):
            return self.gapi_res_not_found.post_git_commit()
        else:
            return self.gapi_res_not_found.response

    def mocked_http_patch_response(self, *args, **kwargs):
        url: str
        data: str
        headers: CaseInsensitiveDict

        if args is None or len(args) == 0:
            url = kwargs['url']
            data = kwargs['data']
            headers = kwargs['headers']
        else:
            url = args[0]
            headers = args[1]
            data = args[2]
        if bool(match(self.git_ref_url, url)):
            return self.gapi_success.patch_git_ref()
        else:
            return self.gapi_success.response


class MockedGithubAPIHandler:
    g_api_mock: GithubAPIMock = GithubAPIMock(for_status=Status.SUCCESS)

    def get_release(self) -> list[GithubRelease]:
        return [GithubRelease(data=self.g_api_mock.get_latest_release().data)]

    def get_tag(self, *args, **kwargs) -> GithubTag:
        return GithubTag(data=loads(self.g_api_mock.get_tag().data)[0])

    def get_commit(self, *args, **kwargs) -> GithubCommit:
        return GithubCommit(data=self.g_api_mock.get_commit().data)

    def get_commit_blog_page_file(self, *args, **kwargs) -> GithubCommit:
        return GithubCommit(data=self.g_api_mock.get_commit(blog_page_file=True).data)

    def get_commit_blog_file(self, *args, **kwargs) -> GithubCommit:
        return GithubCommit(data=self.g_api_mock.get_commit(blog_file=True).data)

    def get_commit_all_files(self, *args, **kwargs) -> GithubCommit:
        return GithubCommit(data=self.g_api_mock.get_commit(blog_file=True, blog_page_file=True).data)

    def commit_files(self, *args, **kwargs) -> GithubRefObject:
        return GithubRefObject(data=self.g_api_mock.get_latest_ref().data)

    def get_raw_data(self, *args, **kwargs) -> str:
        return self.g_api_mock.get_raw_data()


class MockedGithubAppApi:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def create_access_token(*args, **kwargs) -> GithubAccessToken:
        return mocked_token()
