from lib.data import Repository, GithubRelease, Webhook
from lib.handlers import GithubAPIHandler


class Jobs:
    _webhook: Webhook

    def status(self):
        pass

    @staticmethod
    def push_new_blog_page():
        """ Pushes the new blog-page code to blog repository src folder and then triggers the build workflow to build the new blog pages out of the new release build.

        Returns:

        """
        # repos
        website_repo: Repository = Repository(owner='Coders-Asylum', repo='coders-asylum.github.io', branch='production')
        target_repos: Repository = Repository(owner='Coders-Asylum', repo='blog', branch='master')

        # api object
        github_api: GithubAPIHandler

        release: GithubAPIHandler = GithubAPIHandler(owner=website_repo.owner, repo=website_repo.name, branch=website_repo.branch)
