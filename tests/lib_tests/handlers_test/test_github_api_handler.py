from unittest import TestCase, main, mock

# from requests import get
# from json import loads
# from requests.structures import CaseInsensitiveDict
# from os import environ
from lib.handlers import *

# from datetime import datetime
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.backends import default_backend
# from jwt import encode
from tests.mocks.mocked_classes import MockedResponseHandlers, mocked_token
from tests.mocks.github_api_mocks import GithubAPIMock, Status


class TestGithubAPIHandler(TestCase):
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

    @mock.patch('lib.handlers.ResponseHandlers.http_get_response', side_effect=mockedResponse.mocked_http_get_response)
    def test_download_repo_file(self, mock_func):
        expected_file = self.g_mock_success.download_repo_file()
        file_path: str = 'custom_card_design/test/widget_test.dart'
        _r = self.g.download_repo_file(repo_name=self.repo, owner=self.owner, file_path=file_path,
                                       branch=self.branch)

        self.assertEqual(expected_file.data, _r.data)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response', side_effect=mockedResponse.mocked_http_get_response)
    def test_get_git_ref(self, mock_func):
        r: GithubRefObject = self.g._get_git_ref(self.owner, self.repo, self.branch)
        expected_res = self.g_mock_success.getref()

        expected_res_j = loads(expected_res.data)
        self.assertEqual(r.url, expected_res_j['url'])
        self.assertEqual(r.nodeId, expected_res_j['node_id'])
        self.assertEqual(r.ref, expected_res_j['ref'])
        self.assertEqual(r.obj, expected_res_j['object'])

    @mock.patch('lib.handlers.ResponseHandlers.curl_post_response', side_effect=mockedResponse.mocked_http_post_response)
    def test_post_blob(self, mock_func):  # Data that will be posted to the Github server to create a blob.
        expected_blob: Response = self.g_mock_success.post_blob()
        actual_blob = self.g.post_blob(owner=self.owner, repo=self.repo, data=self.expected_contents, access_token=self.g_mock_success.create_access_token())
        self.assertEqual(loads(expected_blob.data)['url'], actual_blob.url)
        self.assertEqual(loads(expected_blob.data)['sha'], actual_blob.sha)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response', side_effect=mockedResponse.mocked_http_get_response)
    def test_get_latest_commit(self, mock_func):
        commit = self.g._get_latest_commit(owner=self.owner, repo=self.repo, branch=self.branch)
        expected_commit = self.g_mock_success.get_commit()

        self.assertEqual(loads(expected_commit.data)['sha'], commit.sha)
        self.assertEqual(loads(expected_commit.data)['author'], commit.author)
        self.assertEqual(loads(expected_commit.data)['committer'], commit.committer)
        self.assertEqual(loads(expected_commit.data)['message'], commit.message)
        self.assertEqual(loads(expected_commit.data)['tree'], commit.tree)

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response', side_effect=mockedResponse.mocked_http_get_response)
    def test_get_tree(self, mock_func):
        tree = self.g._get_tree(owner=self.owner, repo=self.repo, branch=self.branch)
        expected_tree = self.g_mock_success.get_tree()
        self.assertEqual(loads(expected_tree.data)['sha'], tree.sha)
        self.assertEqual(loads(expected_tree.data)['url'], tree.url)
        self.assertEqual(loads(expected_tree.data)['tree'], tree.tree)

    # def test_update_and_post_tree(self): expected_contents = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis at tellus at urna condimentum mattis pellentesque id. Lobortis elementum nibh tellus molestie nunc non.
    # Vestibulum lectus mauris ultrices ' \ 'eros in. Odio ut sem nulla pharetra. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Nam libero justo laoreet sit amet cursus. Amet nulla facilisi morbi tempus iaculis urna. Massa id neque aliquam vestibulum morbi blandit cursus risus
    # at. Mi in nulla ' \ 'posuere sollicitudin aliquam ultrices sagittis orci. Lobortis feugiat vivamus at augue eget arcu dictum. Sit amet consectetur adipiscing elit pellentesque. Tortor posuere ac ut consequat semper viverra nam libero justo. Eu nisl nunc mi ipsum faucibus vitae. Semper ' \
    # 9'feugiat nibh sed pulvinar proin gravida hendrerit. Habitant morbi tristique senectus et netus et. Tempor orci dapibus ultrices in iaculis nunc. Amet risus nullam eget felis eget nunc lobortis mattis. Posuere sollicitudin aliquam ultrices sagittis orci. '
    #
    #     tree = [GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=expected_contents)]
    #     posted_tree = self.g.update_and_post_tree(owner=self.owner, repo=self.repo, branch=self.branch, files=tree)
    #     actual_tree = get(url=f'https://api.github.com/repos/octocat/hello-world/git/trees/{posted_tree.sha}?recursive=1')
    #     if actual_tree.status_code != 200:
    #         self.fail(f'Posted tree with sha: {posted_tree.sha} failed to get due to: {actual_tree.status_code} {actual_tree.reason}')
    #     else:
    #         actual_tree_data = loads(actual_tree.text)['tree']
    #         expected_tree_data = loads(posted_tree.tree)
    #         self.assertEqual(actual_tree_data, expected_tree_data)

    def test_commit_files(self):
        pass

    @mock.patch('lib.handlers.ResponseHandlers.curl_get_response', side_effect=mockedResponse.mocked_http_get_response)
    def test_get_latest_release(self, mock_func):
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
