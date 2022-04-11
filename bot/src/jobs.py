import os.path
from json import load, dumps
from logging import info
from os import environ
from lib import Response
from lib.data import Repository, GithubRelease, Webhook, GithubCommit, Message, GitTree, TreeType
from lib.handlers import GithubAPIHandler, GithubAccessToken, GithubAppApi


class Jobs:
    _webhook: Webhook
    _response: Response
    __config_file_path: str = os.path.join(os.path.dirname(__file__), './res/config.json')

    def __init__(self):
        self._response = Response(status_code=202, status='Accepted', data=Message.no_processing_required)
        config_file = open(self.__config_file_path)
        self.config_data: dict = load(config_file)
        config_file.close()

    def push_new_blog_page(self) -> Response:
        """ Pushes the new blog-page code to blog repository src folder and then triggers the build workflow to build the new blog pages out of the new release build.

        Returns:

        """
        payload: list = []
        # repos
        website_repo: Repository = Repository(owner='Coders-Asylum', repo='coders-asylum.github.io', branch='production')
        target_repos: Repository = Repository(owner='Coders-Asylum', repo='blog', branch='master')

        # github app api
        g_app_api: GithubAppApi = GithubAppApi(app_id=environ.get('APP_ID'))

        # api object
        github_api_website: GithubAPIHandler = GithubAPIHandler(owner=website_repo.owner, repo=website_repo.name, branch=website_repo.branch)
        github_api_target: GithubAPIHandler = GithubAPIHandler(owner=target_repos.owner, repo=target_repos.name, branch=website_repo.branch)

        # get release data
        release: list[GithubRelease] = github_api_website.get_release()

        # get tag commit
        tag_commit: dict = github_api_website.get_tag(tag_name=release[0].tag).commit

        commit: GithubCommit = github_api_website.get_commit(sha=tag_commit['sha'])

        if commit.files is None or commit.files == []:
            return self._response

        target_access_tkn: GithubAccessToken = g_app_api.create_access_token(org=target_repos.owner, repos=[target_repos.name], permissions=None)
        for f in commit.files:
            # update blog page file
            if f['filename'] == self.config_data['blog_page']['path']:
                blog_page_file_content: str = github_api_website.get_raw_data(path=self.config_data['blog_page']['path'])
                blog_page_tree: GitTree = GitTree(tree_type=TreeType.BLOB, path=self.config_data['blog_page']['path'], content=blog_page_file_content)
                github_api_target.set_token(access_tkn=target_access_tkn)

                target_ref = github_api_target.commit_files(files=[blog_page_tree], message=f'New Release: {release[0].tag} \n link: https://github.com/{website_repo.owner}/{website_repo.name}/releases/tag/{release[0].tag}')
                info(f'[I] New Blog Page File Committed url:{target_ref.url}')
                payload.append(f'New Blog Page File Committed url:{target_ref.url}')
                self._response.status_code = 200

            # update blog page file
            elif f['filename'] == self.config_data['blog_post_page']['path']:
                blog_post_page_file_content: str = github_api_website.get_raw_data(path=self.config_data['blog_post_page']['path'])
                blog_post_page_tree: GitTree = GitTree(tree_type=TreeType.BLOB, path=self.config_data['blog_page']['path'], content=blog_post_page_file_content)
                github_api_target.set_token(access_tkn=target_access_tkn)

                target_ref = github_api_target.commit_files(files=[blog_post_page_tree], message=f'New Release: {release[0].tag} \n link: https://github.com/{website_repo.owner}/{website_repo.name}/releases/tag/{release[0].tag}')
                info(f'[I] New Blog Post Page File Committed url:{target_ref.url}')
                payload.append(f'New Blog Page File Committed url:{target_ref.url}')
                self._response.status_code = 200

        if payload:
            self._response.data = dumps({"message": payload})

        return self._response
