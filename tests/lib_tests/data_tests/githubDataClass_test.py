from unittest import main, TestCase

from lib.data.githubDataClass import Repository


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


if __name__ == "__main__":
    main()
