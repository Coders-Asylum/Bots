from json import loads, dumps
from unittest import TestCase, main, mock
from requests.structures import CaseInsensitiveDict
from lib.data.constants import Status as internal_status
from lib.data import *
from lib.handlers import *

# from datetime import datetime
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.backends import default_backend
# from jwt import encode
from tests.mocks.mocked_classes import MockedResponseHandlers, mocked_token
from tests.mocks.github_api_mocks import GithubAPIMock, Status


class TestGithubAPIHandler4xxFailed(TestCase):
    """ Tests for implemented APIs HTTP responses returning as resource not found or failed (4xx errors)
    """
    mockedResponse: MockedResponseHandlers = MockedResponseHandlers()

    owner = 'Coders-Asylum'
    repo = 'fuzzy-train'
    branch = 'test_branch'
    test_token: str = 'ghs_BWpGokQJ7kJe4vWWir7xLgN6ciyA7e0fDka8'

    g: GithubAPIHandler = GithubAPIHandler(owner=owner, repo=repo, branch=branch)
    g_mock_res_not_found: GithubAPIMock = GithubAPIMock(for_status=Status.RES_NOT_FOUND)
    g_mock_success: GithubAPIMock = GithubAPIMock(for_status=Status.SUCCESS)
    __internal_status = internal_status()

    header: CaseInsensitiveDict = CaseInsensitiveDict()
    header['Accept'] = 'application/vnd.github.v3+json'

    expected_contents = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis at tellus at urna condimentum mattis pellentesque id. Lobortis elementum nibh tellus molestie nunc non. Vestibulum lectus mauris ultrices ' \
                        'eros in. Odio ut sem nulla pharetra. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Nam libero justo laoreet sit amet cursus. Amet nulla facilisi morbi tempus iaculis urna. Massa id neque aliquam vestibulum morbi blandit cursus risus at. Mi in nulla ' \
                        'posuere sollicitudin aliquam ultrices sagittis orci. Lobortis feugiat vivamus at augue eget arcu dictum. Sit amet consectetur adipiscing elit pellentesque. Tortor posuere ac ut consequat semper viverra nam libero justo. Eu nisl nunc mi ipsum faucibus vitae. Semper ' \
                        'feugiat nibh sed pulvinar proin gravida hendrerit. Habitant morbi tristique senectus et netus et. Tempor orci dapibus ultrices in iaculis nunc. Amet risus nullam eget felis eget nunc lobortis mattis. Posuere sollicitudin aliquam ultrices sagittis orci. '

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_raw_data_404_error(self, mock_func):
        _expected_msg: str = 'ERROR:root:Error while getting file contents\nResponse data from get_raw_data api: \n\t404 Resource not found\n\tNot found\n-----------------------------------------------------'
        mock_func.side_effect = self.mockedResponse.mocked_http_get_res_found_response
        file_path: str = 'custom_card_design/test/widget_test.dart'
        with self.assertRaises(expected_exception=GithubApiException) as api_exception:
            _r = self.g.get_raw_data(path=file_path)
        self.assertEqual(api_exception.exception.response.data, self.g_mock_res_not_found.get_raw_data().data)
        self.assertEqual(api_exception.exception.response.status, self.g_mock_res_not_found.get_raw_data().status)
        self.assertEqual(api_exception.exception.response.status_code, self.g_mock_res_not_found.get_raw_data().status_code)

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    def test_post_blob(self, mock_func):  # Data that will be posted to the Github server to create a blob.
        mock_func.side_effect = self.mockedResponse.mocked_http_post_res_not_response
        expected_blob: Response = self.g_mock_res_not_found.post_blob()
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.post_blob(data=self.expected_contents)

        self.assertEqual(api_exception.exception.response.data, expected_blob.data)
        self.assertEqual(api_exception.exception.response.status, expected_blob.status)
        self.assertEqual(api_exception.exception.response.status_code, expected_blob.status_code)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    @mock.patch('lib.handlers.ResponseHandlers.http_patch')
    def test_commit_files_access_token_not_set(self, mock_patch, mock_post, mock_get):
        # mocks
        mock_get.side_effect = self.mockedResponse.mocked_http_get_response
        mock_post.side_effect = self.mockedResponse.mocked_http_post_response
        mock_patch.side_effect = self.mockedResponse.mocked_http_patch_response

        file: GitTree = GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=self.expected_contents)
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.commit_files(files=[file], message='New test file')

        self.assertEqual(api_exception.exception.response.status, self.__internal_status.program_error['status'])
        self.assertEqual(api_exception.exception.response.status_code, self.__internal_status.program_error['status_code'])
        self.assertEqual(api_exception.exception.response.data, '{message: API Token Not Set}')

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    @mock.patch('lib.handlers.ResponseHandlers.http_patch')
    def test_commit_files_get_request_failed(self, mock_patch, mock_post, mock_get):
        # mocks
        mock_get.side_effect = self.mockedResponse.mocked_http_get_res_found_response
        mock_post.side_effect = self.mockedResponse.mocked_http_post_response
        mock_patch.side_effect = self.mockedResponse.mocked_http_patch_response

        expected_res = self.g_mock_res_not_found.get_latest_ref()

        file: GitTree = GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=self.expected_contents)
        self.g.set_token(access_tkn=mocked_token())
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.commit_files(files=[file], message='New test file')

        self.assertEqual(api_exception.exception.response.status, expected_res.status)
        self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    @mock.patch('lib.handlers.ResponseHandlers.http_patch')
    def test_commit_files_post_request_failed(self, mock_patch, mock_post, mock_get):
        # mocks
        mock_get.side_effect = self.mockedResponse.mocked_http_get_response
        mock_post.side_effect = self.mockedResponse.mocked_http_post_res_not_response
        mock_patch.side_effect = self.mockedResponse.mocked_http_patch_response

        # expected_res = self.g_mock_res_not_found.post_git_tree()

        file: GitTree = GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=self.expected_contents)
        self.g.set_token(access_tkn=mocked_token())
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.commit_files(files=[file], message='New test file')

        # self.assertEqual(api_exception.exception.response.status, expected_res.status)
        # self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    @mock.patch('lib.handlers.ResponseHandlers.http_patch')
    def test_commit_files_patch_request_failed(self, mock_patch, mock_post, mock_get):
        # mocks
        mock_get.side_effect = self.mockedResponse.mocked_http_get_response
        mock_post.side_effect = self.mockedResponse.mocked_http_post_response
        mock_patch.side_effect = self.mockedResponse.mocked_http_patch_res_not_found_response

        # expected_res = self.g_mock_res_not_found.patch_git_ref()

        file: GitTree = GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=self.expected_contents)
        self.g.set_token(access_tkn=mocked_token())
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.commit_files(files=[file], message='New test file')

        # self.assertEqual(api_exception.exception.response.status, expected_res.status)
        # self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_latest_release(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_get_res_found_response
        expected_data = self.g_mock_res_not_found.get_latest_release()
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.get_release()

        self.assertEqual(api_exception.exception.response.data, expected_data.data)
        self.assertEqual(api_exception.exception.response.status_code, expected_data.status_code)
        self.assertEqual(api_exception.exception.response.status, expected_data.status)

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    def test_trigger_workflow(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_post_res_not_response

        # setting a mock token
        self.g.set_token(access_tkn=mocked_token())
        expected_data = self.g_mock_res_not_found.trigger_workflow()

        inputs: dict = {"name": "test"}
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.trigger_workflow(name='manual.yml', ref="main", inputs=inputs)

        self.assertEqual(api_exception.exception.response.data, expected_data.data)
        self.assertEqual(api_exception.exception.response.status_code, expected_data.status_code)
        self.assertEqual(api_exception.exception.response.status, expected_data.status)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_tags_post_failed(self, mock_func):
        # mock
        mock_func.side_effect = self.mockedResponse.mocked_http_get_res_found_response

        tag: str = 'V0.0.1a'
        expected_res = self.g_mock_res_not_found.get_tag()

        with self.assertRaises(GithubApiException) as api_exception:
            self.g.get_tag(tag_name=tag)

        self.assertEqual(api_exception.exception.response.data, expected_res.data)
        self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)
        self.assertEqual(api_exception.exception.response.status, expected_res.status)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_commit(self, mock_func):
        sha: str = '10f68682850d598a90ed6f5ea237f5b140a5f4f3'
        # mock
        mock_func.side_effect = self.mockedResponse.mocked_http_get_res_found_response

        expected_res = self.g_mock_res_not_found.get_commit()

        with self.assertRaises(GithubApiException) as api_exception:
            self.g.get_commit(sha=sha)

        self.assertEqual(api_exception.exception.response.data, expected_res.data)
        self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)
        self.assertEqual(api_exception.exception.response.status, expected_res.status)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_milestone_404_error(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_get_res_found_response
        expected_res = self.g_mock_res_not_found.get_milestone()

        with self.assertRaises(GithubApiException) as api_exception:
            self.g.get_milestone(name='v1.0')

        self.assertEqual(api_exception.exception.response.data, expected_res.data)
        self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)
        self.assertEqual(api_exception.exception.response.status, expected_res.status)

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    def test_create_issue_res_not_found(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_post_res_not_response
        expected_res = self.g_mock_res_not_found.create_issue()
        with self.assertRaises(GithubApiException) as api_exception:
            self.g.create_issue(title='Test Issue', body='test issue body')

        self.assertEqual(api_exception.exception.response.data, expected_res.data)
        self.assertEqual(api_exception.exception.response.status_code, expected_res.status_code)
        self.assertEqual(api_exception.exception.response.status, expected_res.status)


class TestGithubAPIHandler(TestCase):
    """ Tests for implemented APIs HTTP responses returning as successful
    """
    mockedResponse: MockedResponseHandlers = MockedResponseHandlers()

    owner = 'Coders-Asylum'
    repo = 'fuzzy-train'
    branch = 'test_branch'
    test_token: str = 'ghs_BWpGokQJ7kJe4vWWir7xLgN6ciyA7e0fDka8'

    g: GithubAPIHandler = GithubAPIHandler(owner=owner, repo=repo, branch=branch)
    g_mock_success: GithubAPIMock = GithubAPIMock(for_status=Status.SUCCESS)

    header: CaseInsensitiveDict = CaseInsensitiveDict()
    header['Accept'] = 'application/vnd.github.v3+json'

    expected_contents = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis at tellus at urna condimentum mattis pellentesque id. Lobortis elementum nibh tellus molestie nunc non. Vestibulum lectus mauris ultrices ' \
                        'eros in. Odio ut sem nulla pharetra. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Nam libero justo laoreet sit amet cursus. Amet nulla facilisi morbi tempus iaculis urna. Massa id neque aliquam vestibulum morbi blandit cursus risus at. Mi in nulla ' \
                        'posuere sollicitudin aliquam ultrices sagittis orci. Lobortis feugiat vivamus at augue eget arcu dictum. Sit amet consectetur adipiscing elit pellentesque. Tortor posuere ac ut consequat semper viverra nam libero justo. Eu nisl nunc mi ipsum faucibus vitae. Semper ' \
                        'feugiat nibh sed pulvinar proin gravida hendrerit. Habitant morbi tristique senectus et netus et. Tempor orci dapibus ultrices in iaculis nunc. Amet risus nullam eget felis eget nunc lobortis mattis. Posuere sollicitudin aliquam ultrices sagittis orci. '

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_raw_data(self, mock_func):
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response
        expected_file = self.g_mock_success.download_repo_file()
        file_path: str = 'custom_card_design/test/widget_test.dart'
        _r = self.g.get_raw_data(path=file_path)

        self.assertEqual(expected_file.data, _r)

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    def test_post_blob(self, mock_func):  # Data that will be posted to the Github server to create a blob.
        mock_func.side_effect = self.mockedResponse.mocked_http_post_response
        expected_blob: Response = self.g_mock_success.post_blob()
        self.g.set_token(access_tkn=mocked_token())
        actual_blob = self.g.post_blob(data=self.expected_contents)
        self.assertEqual(loads(expected_blob.data)['url'], actual_blob.url)
        self.assertEqual(loads(expected_blob.data)['sha'], actual_blob.sha)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    @mock.patch('lib.handlers.ResponseHandlers.http_patch')
    def test_commit_files(self, mock_patch, mock_post, mock_get):
        # mocks
        mock_get.side_effect = self.mockedResponse.mocked_http_get_response
        mock_post.side_effect = self.mockedResponse.mocked_http_post_response
        mock_patch.side_effect = self.mockedResponse.mocked_http_patch_response

        expected_ref = loads(self.g_mock_success.patch_git_ref().data)

        posting_contents = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis at tellus at urna condimentum mattis pellentesque id. Lobortis elementum nibh tellus molestie nunc non. Vestibulum lectus mauris ultrices ' \
                           'eros in. Odio ut sem nulla pharetra. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Nam libero justo laoreet sit amet cursus. Amet nulla facilisi morbi tempus iaculis urna. Massa id neque aliquam vestibulum morbi blandit cursus risus at. Mi in nulla ' \
                           'posuere sollicitudin aliquam ultrices sagittis orci. Lobortis feugiat vivamus at augue eget arcu dictum. Sit amet consectetur adipiscing elit pellentesque. Tortor posuere ac ut consequat semper viverra nam libero justo. Eu nisl nunc mi ipsum faucibus vitae. Semper ' \
                           'feugiat nibh sed pulvinar proin gravida hendrerit. Habitant morbi tristique senectus et netus et. Tempor orci dapibus ultrices in iaculis nunc. Amet risus nullam eget felis eget nunc lobortis mattis. Posuere sollicitudin aliquam ultrices sagittis orci. '

        file: GitTree = GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=posting_contents)
        # setting a mock token
        self.g.set_token(access_tkn=mocked_token())
        actual: GithubRefObject = self.g.commit_files(files=[file], message='New test file')

        self.assertEqual(actual.url, expected_ref['url'])
        self.assertEqual(actual.ref, expected_ref['ref'])
        self.assertEqual(actual.obj, expected_ref['object'])
        self.assertEqual(actual.nodeId, expected_ref['node_id'])

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_latest_release(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response
        expected_data = loads(self.g_mock_success.get_latest_release().data)
        actual_release: list[GithubRelease] = self.g.get_release()
        self.assertEqual(actual_release[0].pre_release, expected_data['prerelease'])
        self.assertEqual(actual_release[0].tag, expected_data['tag_name'])
        self.assertEqual(actual_release[0].node_id, expected_data['node_id'])

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_all_release(self, mock_func):
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response

        expected_data = loads(self.g_mock_success.get_latest_release(latest=False).data)
        actual_release: list[GithubRelease] = self.g.get_release(latest=False)
        self.assertEqual(len(actual_release), len(expected_data))
        for i in range(len(expected_data)):
            self.assertEqual(actual_release[i].pre_release, expected_data[i]['prerelease'])
            self.assertEqual(actual_release[i].tag, expected_data[i]['tag_name'])
            self.assertEqual(actual_release[i].node_id, expected_data[i]['node_id'])

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    def test_trigger_workflow(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_post_response

        # setting a mock token
        self.g.set_token(access_tkn=mocked_token())
        expected_data = self.g_mock_success.trigger_workflow().data

        inputs: dict = {"name": "test"}
        actual_res = self.g.trigger_workflow(name='manual.yml', ref="main", inputs=inputs)

        self.assertEqual(expected_data, actual_res.data)
        self.assertEqual(204, actual_res.status_code)
        self.assertEqual('No Content', actual_res.status)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_tags(self, mock_func):
        expected_tag: dict = {}
        tag: str = 'V0.0.1a'
        # mock
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response

        expected_tags: list[dict] = loads(self.g_mock_success.get_tag().data)

        for _tag in expected_tags:
            if _tag['name'] == tag:
                expected_tag = _tag
                break

        actual_tag: GithubTag = self.g.get_tag(tag_name=tag)

        self.assertEqual(expected_tag['name'], actual_tag.name)
        self.assertEqual(expected_tag['commit'], actual_tag.commit)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_tags_non_existing(self, mock_func):
        tag: str = 'not_the_tag'
        # mock
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response

        expected_tag: dict = loads(self.g_mock_success.get_tag().data)[0]

        actual_tag: GithubTag = self.g.get_tag(tag_name=tag)

        self.assertEqual(expected_tag['name'], actual_tag.name)
        self.assertEqual(expected_tag['commit'], actual_tag.commit)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_commit(self, mock_func):
        sha: str = '10f68682850d598a90ed6f5ea237f5b140a5f4f3'

        # mock
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response

        expected_commit = loads(self.g_mock_success.get_commit().data)

        actual_commit: GithubCommit = self.g.get_commit(sha=sha)

        self.assertEqual(expected_commit['sha'], actual_commit.sha)
        self.assertEqual(expected_commit['parents'], actual_commit.parents)
        self.assertEqual(expected_commit['files'], actual_commit.files)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_milestone(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response

        expected_milestone = loads(self.g_mock_success.get_milestone().data)[0]

        actual_milestone: GithubMilestone = self.g.get_milestone(name='v1.0')

        self.assertEqual(actual_milestone.name, expected_milestone['title'])
        self.assertEqual(actual_milestone.number, expected_milestone['number'])
        self.assertEqual(actual_milestone.id, expected_milestone['id'])

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response')
    def test_get_milestone_returns_none(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_get_response
        actual_milestone: GithubMilestone = self.g.get_milestone(name='non_existing_milestone')

        self.assertIsNone(actual_milestone)

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response')
    def test_create_issue(self, mock_func):
        # mocks
        mock_func.side_effect = self.mockedResponse.mocked_http_post_response
        expected_issue = loads(self.g_mock_success.create_issue().data)

        actual_issue: GithubIssue = self.g.create_issue(title='Test Issue', body='test issue body')

        self.assertEqual(actual_issue.id, expected_issue['id'])
        self.assertEqual(actual_issue.url, expected_issue['url'])
        self.assertEqual(actual_issue.number, expected_issue['number'])
        self.assertEqual(actual_issue.state, expected_issue['state'])
        self.assertEqual(actual_issue.title, expected_issue['title'])


class TestAccessTokenPermission(TestCase):

    def test_AccessTokenPermission_all_read(self):
        expected_payload = {'contents': 'read', 'issues': 'read', 'pages': 'read', 'pull_requests': 'read', 'members': 'read'}
        access_tkn_permission: AccessTokenPermission = AccessTokenPermission()

        access_tkn_permission.set(permission=GithubPermissions.CONTENTS, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.ISSUES, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.PAGES, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.PULL_REQUESTS, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.MEMBERS, access=AccessType.READ)

        actual_payload = access_tkn_permission.payload()

        self.assertEqual(expected_payload, actual_payload)

    def test_AccessTokenPermission_all_write(self):
        expected_payload = {'contents': 'write', 'issues': 'write', 'pages': 'write', 'pull_requests': 'write', 'members': 'write'}
        access_tkn_permission: AccessTokenPermission = AccessTokenPermission()

        access_tkn_permission.set(permission=GithubPermissions.CONTENTS, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.ISSUES, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.PAGES, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.PULL_REQUESTS, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.MEMBERS, access=AccessType.WRITE)

        actual_payload = access_tkn_permission.payload()

        self.assertEqual(expected_payload, actual_payload)

    def test_AccessTokenPermission_on_change(self):
        expected_payload = {'contents': 'read', 'issues': 'write', 'pages': 'read', 'pull_requests': 'write', 'members': 'write'}
        expected_payload_on_change = {'contents': 'read', 'issues': 'write', 'pull_requests': 'read', 'pages': 'read', 'members': 'write'}
        access_tkn_permission: AccessTokenPermission = AccessTokenPermission()

        access_tkn_permission.set(permission=GithubPermissions.CONTENTS, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.ISSUES, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.PAGES, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.PULL_REQUESTS, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.MEMBERS, access=AccessType.WRITE)

        actual_payload = access_tkn_permission.payload()

        self.assertEqual(expected_payload, actual_payload)
        # remove pages permission for the object
        access_tkn_permission.set(permission=GithubPermissions.PULL_REQUESTS, access=AccessType.READ)
        actual_payload = access_tkn_permission.payload()

        self.assertEqual(expected_payload_on_change, actual_payload)

    def test_AccessTokenPermission_all_del(self):
        expected_payload = {'contents': 'read', 'issues': 'write', 'pages': 'read', 'pull_requests': 'write', 'members': 'write'}
        expected_payload_on_del = {'contents': 'read', 'issues': 'write', 'pull_requests': 'write', 'members': 'write'}
        access_tkn_permission: AccessTokenPermission = AccessTokenPermission()

        access_tkn_permission.set(permission=GithubPermissions.CONTENTS, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.ISSUES, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.PAGES, access=AccessType.READ)
        access_tkn_permission.set(permission=GithubPermissions.PULL_REQUESTS, access=AccessType.WRITE)
        access_tkn_permission.set(permission=GithubPermissions.MEMBERS, access=AccessType.WRITE)

        actual_payload = access_tkn_permission.payload()

        self.assertEqual(expected_payload, actual_payload)
        # remove pages permission for the object
        access_tkn_permission.set(permission=GithubPermissions.PAGES, access=AccessType.NULL)
        actual_payload = access_tkn_permission.payload()

        self.assertEqual(expected_payload_on_del, actual_payload)


class TestGithubAppApi(TestCase):
    # app = GithubAppApi(app_id=environ.get('APP_ID'))

    def test_get_app_installations(self):
        pass
        # with open('__path__ tpfile ', 'rb') as cert_file:
        #     _pvt = serialization.load_pem_private_key(data=cert_file.read(), password=None, backend=default_backend)
        # actual_list = self.app.get_app_installations()
        # cur_time = int(round(datetime.now().timestamp()))
        # payload = {"iat": cur_time, "exp": cur_time + (60 * 5), "iss": environ.get("APP_ID")}
        # encoded = encode(payload=payload, key=_pvt, algorithm="RS256")
        # headers = CaseInsensitiveDict()
        # headers["Authorization"] = "Bearer " + encoded
        # headers["Accept"] = "application/vnd.github.v3+json"
        #
        # url = "https://api.github.com/app/installations"
        # req = get(url=url, headers=headers)
        # if req.status_code != 200:
        #     self.fail(f'Unable to fetch app installations due to: {req.status_code} {req.text}')
        # expected_list = loads(req.text)
        #
        # self.assertEqual(len(actual_list), len(expected_list))
        # for i in range(len(actual_list)):
        #     self.assertEqual(actual_list[i].org, expected_list[i]['account']['login'])
        #     self.assertEqual(actual_list[i].install_id, expected_list[i]['id'])
        #     self.assertEqual(actual_list[i].acc_tkn_url, expected_list[i]['access_tokens_url'])


class TestGithubRelease(TestCase):
    mock_api_data = GithubAPIMock(for_status=Status.SUCCESS)
    expected_data = loads(mock_api_data.get_latest_release().data)

    def test_data_extraction(self):
        release = GithubRelease(data=dumps(self.expected_data))
        self.assertEqual(release.pre_release, self.expected_data['prerelease'])
        self.assertEqual(release.tag, self.expected_data['tag_name'])
        self.assertEqual(release.node_id, self.expected_data['node_id'])


if __name__ == '__main__':
    main()
