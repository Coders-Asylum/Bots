from unittest import main, TestCase

from lib.data.githubDataClass import *
from tests.mocks.github_api_mocks import GithubAPIMock, Status


class Repository_tests(TestCase):
    owner = "Coders-Asylum"
    repo = "fuzzy-train"
    branch = "test_branch"

    def test_data_class(self):
        repo = Repository(owner=self.owner, repo=self.repo, branch=self.branch)

        self.assertEqual(repo.owner, self.owner)
        self.assertEqual(repo.branch, self.branch)
        self.assertEqual(repo.name, self.repo)

    def test_get_item(self):
        repo = Repository(owner=self.owner, repo=self.repo, branch=self.branch)

        self.assertEqual(repo['owner'], self.owner)
        self.assertEqual(repo['branch'], self.branch)
        self.assertEqual(repo['name'], self.repo)


class GithubTag_tests(TestCase):
    g_api_mock: GithubAPIMock = GithubAPIMock(for_status=Status.SUCCESS)
    expected_tag = loads(g_api_mock.get_tag().data)[0]

    def test_data_class(self):
        actual: GithubTag = GithubTag(self.expected_tag)

        self.assertEqual(actual.name, self.expected_tag['name'])
        self.assertEqual(actual.commit, self.expected_tag['commit'])


if __name__ == "__main__":
    main()