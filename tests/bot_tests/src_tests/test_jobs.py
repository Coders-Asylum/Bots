from json import dumps
from unittest import TestCase, main, mock

from bot.src import Jobs
from lib.handlers import Response
from tests.mocks.mocked_classes import MockedGithubAPIHandler, MockedGithubAppApi


class TestJobs(TestCase):
    g_api_mock = MockedGithubAPIHandler()
    g_app_api_mock = MockedGithubAppApi()

    @mock.patch('lib.handlers.GithubAppApi.__init__')
    @mock.patch('lib.handlers.GithubAPIHandler.get_release')
    @mock.patch('lib.handlers.GithubAPIHandler.get_tag')
    @mock.patch('lib.handlers.GithubAPIHandler.get_commit')
    @mock.patch('lib.handlers.GithubAppApi.create_access_token')
    @mock.patch('lib.handlers.GithubAPIHandler.get_raw_data')
    @mock.patch('lib.handlers.GithubAPIHandler.commit_files')
    def test_push_new_blog_page_both_file_update(self, commit_files_mock, get_raw_data_mock, create_access_token_mock, get_commit_mock, get_tag_mock, get_releases_mock, mock_app_api):
        # mocked patches
        commit_files_mock.side_effect = self.g_api_mock.commit_files
        get_raw_data_mock.side_effect = self.g_api_mock.get_raw_data
        create_access_token_mock.side_effect = self.g_app_api_mock.create_access_token
        get_commit_mock.side_effect = self.g_api_mock.get_commit_all_files
        get_tag_mock.side_effect = self.g_api_mock.get_tag
        get_releases_mock.side_effect = self.g_api_mock.get_release
        mock_app_api.return_value = None

        jobs = Jobs()
        expected_response = Response(status_code=200, status='Accepted',
                                     data=dumps({"message": ["New Blog Page File Committed url:https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch", "New Blog Page File Committed url:https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch"]}))
        actual_res = jobs.push_new_blog_page()

        self.assertEqual(actual_res.status_code, expected_response.status_code)
        self.assertEqual(actual_res.status, expected_response.status)
        self.assertEqual(actual_res.data, expected_response.data)

    @mock.patch('lib.handlers.GithubAppApi.__init__')
    @mock.patch('lib.handlers.GithubAPIHandler.get_release')
    @mock.patch('lib.handlers.GithubAPIHandler.get_tag')
    @mock.patch('lib.handlers.GithubAPIHandler.get_commit')
    @mock.patch('lib.handlers.GithubAppApi.create_access_token')
    @mock.patch('lib.handlers.GithubAPIHandler.get_raw_data')
    @mock.patch('lib.handlers.GithubAPIHandler.commit_files')
    def test_push_new_blog_page_blog_file_update(self, commit_files_mock, get_raw_data_mock, create_access_token_mock, get_commit_mock, get_tag_mock, get_releases_mock, mock_app_api):
        # mocked patches
        commit_files_mock.side_effect = self.g_api_mock.commit_files
        get_raw_data_mock.side_effect = self.g_api_mock.get_raw_data
        create_access_token_mock.side_effect = self.g_app_api_mock.create_access_token
        get_commit_mock.side_effect = self.g_api_mock.get_commit_blog_file
        get_tag_mock.side_effect = self.g_api_mock.get_tag
        get_releases_mock.side_effect = self.g_api_mock.get_release
        mock_app_api.return_value = None

        jobs = Jobs()
        expected_response = Response(status_code=200, status='Accepted', data=dumps({"message": ["New Blog Page File Committed url:https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch"]}))
        actual_res = jobs.push_new_blog_page()

        self.assertEqual(actual_res.status_code, expected_response.status_code)
        self.assertEqual(actual_res.status, expected_response.status)
        self.assertEqual(actual_res.data, expected_response.data)

    @mock.patch('lib.handlers.GithubAppApi.__init__')
    @mock.patch('lib.handlers.GithubAPIHandler.get_release')
    @mock.patch('lib.handlers.GithubAPIHandler.get_tag')
    @mock.patch('lib.handlers.GithubAPIHandler.get_commit')
    @mock.patch('lib.handlers.GithubAppApi.create_access_token')
    @mock.patch('lib.handlers.GithubAPIHandler.get_raw_data')
    @mock.patch('lib.handlers.GithubAPIHandler.commit_files')
    def test_push_new_blog_page_blog_page_file_update(self, commit_files_mock, get_raw_data_mock, create_access_token_mock, get_commit_mock, get_tag_mock, get_releases_mock, mock_app_api):
        # mocked patches
        commit_files_mock.side_effect = self.g_api_mock.commit_files
        get_raw_data_mock.side_effect = self.g_api_mock.get_raw_data
        create_access_token_mock.side_effect = self.g_app_api_mock.create_access_token
        get_commit_mock.side_effect = self.g_api_mock.get_commit_blog_page_file
        get_tag_mock.side_effect = self.g_api_mock.get_tag
        get_releases_mock.side_effect = self.g_api_mock.get_release
        mock_app_api.return_value = None

        jobs = Jobs()
        expected_response = Response(status_code=200, status='Accepted', data=dumps({"message": ["New Blog Page File Committed url:https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch"]}))
        actual_res = jobs.push_new_blog_page()

        self.assertEqual(actual_res.status_code, expected_response.status_code)
        self.assertEqual(actual_res.status, expected_response.status)
        self.assertEqual(actual_res.data, expected_response.data)

    @mock.patch('lib.handlers.GithubAppApi.__init__')
    @mock.patch('lib.handlers.GithubAPIHandler.get_release')
    @mock.patch('lib.handlers.GithubAPIHandler.get_tag')
    @mock.patch('lib.handlers.GithubAPIHandler.get_commit')
    @mock.patch('lib.handlers.GithubAppApi.create_access_token')
    @mock.patch('lib.handlers.GithubAPIHandler.get_raw_data')
    @mock.patch('lib.handlers.GithubAPIHandler.commit_files')
    def test_push_new_blog_page_no_file_update(self, commit_files_mock, get_raw_data_mock, create_access_token_mock, get_commit_mock, get_tag_mock, get_releases_mock, mock_app_api):
        # mocked patches
        commit_files_mock.side_effect = self.g_api_mock.commit_files
        get_raw_data_mock.side_effect = self.g_api_mock.get_raw_data
        create_access_token_mock.side_effect = self.g_app_api_mock.create_access_token
        get_commit_mock.side_effect = self.g_api_mock.get_commit
        get_tag_mock.side_effect = self.g_api_mock.get_tag
        get_releases_mock.side_effect = self.g_api_mock.get_release
        mock_app_api.return_value = None

        jobs = Jobs()
        expected_response = Response(status_code=202, status='Accepted', data=dumps({"message": "Current payload does not require any processing"}))
        actual_res = jobs.push_new_blog_page()

        self.assertEqual(actual_res.status_code, expected_response.status_code)
        self.assertEqual(actual_res.status, expected_response.status)
        self.assertEqual(actual_res.data, expected_response.data)


if __name__ == "__main__":
    main()
