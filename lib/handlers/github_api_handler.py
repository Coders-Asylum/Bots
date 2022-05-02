import logging
from typing import Union

from lib.data.constants import Status
from lib.handlers.response_handler import ResponseHandlers, Response
from lib.handlers.authHandler import generate_jwt_token, GithubAccessToken
from lib.data import GitCommit, AccessType, GithubPermissions, GithubMilestone, ExceptionType, GithubApiException, GithubAppApiException, GithubAppInstallations, GithubBlob, GithubCommit, GithubIssue, GithubRefObject, GithubRelease, GitTree, GithubTreeObject, GithubTag
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from json import loads, dumps


class AccessTokenPermission:
    """
       Permissions that the access token will be assigned for
       These are the permissions that are available in `properties for permission parameter <https://docs.github.com/en/rest/reference/apps#create-an-installation-access-token-for-an-app--parameters>`
       To know about the permission look in to this part of the `Github api <https://docs.github.com/en/rest/reference/permissions-required-for-github-apps>`
    """
    _permissions: dict = {}

    def __init__(self):
        self._permissions = {}

    def set(self, permission: GithubPermissions, access: AccessType) -> None:
        """
        Set and update the permission for the current object.

        Args:
            permission (GithubPermissions): Permissions to be added or changed from the available GithubPermissions.
            access (AccessType): Access type can be read or write, to remove a permission set `AccessType.NULL` .
        """
        if permission.value in self._permissions.keys():
            if access != AccessType.NULL:
                self._permissions.update({permission.value: access.value})
            else:
                self._permissions.pop(permission.value)
        else:
            self._permissions[permission.value] = access.value

    def payload(self) -> dict:
        """
        The payload that needs to be passed to permission parameter.

        Returns:
        dict_object (dict): A mapped payload for containing all the permissions with the access type.

        """
        if len(self._permissions) == 0:
            return {}
        for permission, access in self._permissions.items():
            if access == 'NULL':
                # todo: change this with custom exception handler and then stop app or process.
                raise Exception(f'A Null type permission present for permission key:{permission}')

        return self._permissions


class GithubAPIHandler:
    _header: CaseInsensitiveDict = CaseInsensitiveDict()
    _latest_commit_sha: str = ''
    owner: str
    branch: str
    repo: str
    __access_token: GithubAccessToken = None

    def __init__(self, owner: str, repo: str, branch: str):
        self._header['Accept'] = 'application/vnd.github.v3+json'
        self.branch = branch
        self.owner = owner
        self.repo = repo
        self.__internal_status = Status()

    def set_token(self, access_tkn: GithubAccessToken) -> None:
        """Sets new token

        Args:
            access_tkn: New GithubAccessToken

        Returns: None

        """
        self.__access_token = access_tkn

    def get_raw_data(self, path: str) -> str:
        """Returns raw contents of the file specified in the path from the branch specified.

        Args:
            path: path to file on the branch with filename and extension

        Returns: file contents as string

        """
        url: str = f'https://raw.githubusercontent.com/{self.owner}/{self.repo}/{self.branch}/{path}'
        _r: Response = ResponseHandlers.curl_get_response(url=url, headers=self._header)
        if _r.status_code != 200:
            raise GithubApiException(msg='Error while getting file contents', api='get_raw_data', response=_r, error_type=ExceptionType.ERROR)
        return _r.data

    def post_blob(self, owner: str, repo: str, data: str, access_token: GithubAccessToken):
        """

        Args:
            owner:
            repo:
            data:
            access_token:

        Returns:

        """
        url: str = f'https://api.github.com/repos/{owner}/{repo}/git/blobs'
        self._header['Authorization'] = f'token {access_token.access_tkn}'
        _data: str = dumps({"content": data})

        _r: Response = ResponseHandlers.curl_post_response(url=url, headers=self._header, data=_data)
        if _r.status_code != 201:
            raise GithubApiException(msg='Blob not posted.', response=_r, error_type=ExceptionType.ERROR, api='post_blob')

        return GithubBlob(data=_r.data)

    def commit_files(self, files: list[GitTree], message: str = 'New commit') -> GithubRefObject:
        """To commit files into the repository.

        Args:
            files (list[GitTree]: Files that needs to be committed
            message (str): Commit message

        Returns: GitHub Ref object after new committed files.

        """
        tree: list[dict] = []
        ref_url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/git/refs/heads/{self.branch}'
        post_tree_url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/git/trees'
        commit_url = f'https://api.github.com/repos/{self.owner}/{self.repo}/git/commits'

        # exception raised if access token not set.
        if self.__access_token is None:
            raise GithubApiException(
                msg='Access token not found, use set_token function to set the token and then proceed',
                error_type=ExceptionType.ERROR,
                response=Response(status_code=self.__internal_status.program_error['status_code'], status=self.__internal_status.program_error['status'], data='{message: API Token Not Set}'),
                api='commit_files'
            )
        self._header['Authorization'] = f'token {self.__access_token.access_tkn}'

        # get branch ref
        _r: Response = ResponseHandlers.curl_get_response(url=ref_url, headers=self._header)
        if _r.status_code != 200:
            raise GithubApiException(msg=f'Error while getting latest git ref for {ref_url}', api='commit_files', error_type=ExceptionType.ERROR, response=_r)
        _ref: GithubRefObject = GithubRefObject(data=_r.data)

        # get and store the latest git commit object from ref
        _r = ResponseHandlers.curl_get_response(url=_ref.obj['url'], headers=self._header)
        if _r.status_code != 200:
            raise GithubApiException(msg=f'Error while getting git commit object for {_ref.obj["url"]}', api='commit_files', error_type=ExceptionType.ERROR, response=_r)
        _commit: GitCommit = GitCommit(data=_r.data)
        self._latest_commit_sha = _commit.sha

        # get the git tree
        # recursive=1 at the end of the tree url helps to get tree objects for all the files with any depth in the repo.
        _r = ResponseHandlers.curl_get_response(url=_commit.tree['url'] + '?recursive=1', headers=self._header)
        if _r.status_code != 200:
            raise GithubApiException(msg=f'Error while getting git tree for: {_commit.tree["url"]}', api='commit_files', response=_r, error_type=ExceptionType.ERROR)
        _git_tree: GithubTreeObject = GithubTreeObject(data=_r.data)

        # update and post tree
        base_tree = _git_tree.sha
        # adding/updating new files
        for file in files:
            if file.content is None and file.sha == 'delete':
                tree.append({"path": file.path, "mode": file.mode, "type": file.type})
            elif file.content is None:
                tree.append({"path": file.path, "mode": file.mode, "type": file.type, "sha": file.sha})
            else:
                tree.append({"path": file.path, "mode": file.mode, "type": file.type, "content": file.content})

        _posting_tree: dict = {"owner": self.owner, "repo": self.repo, "tree": tree, "base_tree": base_tree}
        _r = ResponseHandlers.curl_post_response(url=post_tree_url, headers=self._header, data=dumps(_posting_tree))
        if _r.status_code != 201:
            raise GithubApiException(msg=f'Error while posting new git tree. url: {post_tree_url}', api='commit_files', response=_r, error_type=ExceptionType.ERROR)
        _posted_tree: GithubTreeObject = GithubTreeObject(data=_r.data)

        # commit new tree
        commit_data = {"owner": self.owner, "repo": self.repo, "message": message, "tree": _posted_tree.sha, "parents": [self._latest_commit_sha]}
        _r = ResponseHandlers.curl_post_response(url=commit_url, headers=self._header, data=dumps(commit_data))
        if _r.status_code != 201:
            raise GithubApiException(msg=f'Error while committing . url: {commit_url}', api='commit_files', response=_r, error_type=ExceptionType.ERROR)
        _commit: GitCommit = GitCommit(data=_r.data)

        # update branch ref
        _ref: dict = {"sha": _commit.sha}
        _r: Response = ResponseHandlers.http_patch(url=ref_url, headers=self._header, data=dumps(_ref))
        if _r.status_code != 200:
            raise GithubApiException(msg=f'Error while updating ref. url: {ref_url}', api='commit_files', response=_r, error_type=ExceptionType.ERROR)
        return GithubRefObject(data=_r.data)

    def get_release(self, latest: bool = True) -> list[GithubRelease]:
        """Gets the repository releases

        Args:
            latest (bool): To get the only latest release from the repository. Defaults to True

        Returns: list of GitHub Releases

        """
        if latest:
            url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest'
        else:
            url = f'https://api.github.com/repos/{self.owner}/{self.repo}/releases'

        res: Response = ResponseHandlers.curl_get_response(url=url, headers=self._header)
        if res.status_code != 200:
            raise GithubApiException(msg=f'Error while getting latest release: url = {url}', api='get_release', error_type=ExceptionType.ERROR, response=res)

        if latest:
            return [GithubRelease(data=res.data)]
        else:
            _l: list = []
            for i in loads(res.data):
                _l.append(GithubRelease(data=dumps(i)))
            return _l

    def trigger_workflow(self, name: str, ref: str = 'master', inputs: dict = None):
        """ Triggers the specified workflow using an HTTP call.

        Args:
            name (str): file name with extension of the workflow to be triggered.
            ref (str): The branch/ref on which the action should run is defaulted to master branch.
            inputs (dict): inputs to be given to the action as per specified in the action file.

        Returns (Response): Response object

        """
        if self.__access_token is None:
            raise Exception('[E] Access token not found, use set_token to set the token and then proceed')
        self._header['Authorization'] = f'token {self.__access_token.access_tkn}'
        data: dict = {"ref": ref}
        if inputs is None:
            data["inputs"] = inputs

        url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/actions/workflows/{name}/dispatches'

        res: Response = ResponseHandlers.curl_post_response(url=url, headers=self._header, data=dumps(data))
        if res.status_code != 204:
            raise GithubApiException(msg=f'Error while triggering workflow: url = {url}', api='trigger_workflow', error_type=ExceptionType.ERROR, response=res)

        return res

    def get_tag(self, tag_name: str) -> GithubTag:
        url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/tags'

        res: Response = ResponseHandlers.curl_get_response(url=url, headers=self._header)
        if res.status_code != 200:
            raise GithubApiException(msg=f'Unable to fetch tags. url: {url}', response=res, api='get_tag', error_type=ExceptionType.ERROR)

        tags: list = loads(res.data)
        for tag in tags:
            if tag['name'] == tag_name:
                return GithubTag(tag)

        print(f'[E] specified tag `{tag_name}` not found, returning the latest tag instead')
        return GithubTag(tags[0])

    def get_commit(self, sha: str) -> GithubCommit:
        """Gets Github Commit data using API.

        **Note: this gets the Github Commit object and not Git Commit object**

        Args:
            sha (str): sha string of the commit that is to be fetched.

        Returns: GithubCommit object.

        """
        url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/commits/{sha}'

        res: Response = ResponseHandlers.curl_get_response(url=url, headers=self._header)
        if res.status_code != 200:
            raise GithubApiException(msg=f'Error while getting commit: url = {url}', api='get_commit', error_type=ExceptionType.ERROR, response=res)

        return GithubCommit(data=res.data)

    def get_milestone(self, name: str) -> Union[GithubMilestone, None]:
        """ Gets the milestone details for the given milestone name.

        **Note: implement exception handler because GithubApiException is raised for Error type warning to log this.**

        Args:
            name (str): Milestone name

        Returns (GithubMilestone): GithubMilestone object or None is returned of milestone is not present for the repo.
        """

        url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/milestones'

        res: Response = ResponseHandlers.curl_get_response(url=url, headers=self._header)
        if res.status_code != 200:
            raise GithubApiException(msg=f'Unable to get milestone/s for url={url}', api='get_milestone', response=res, error_type=ExceptionType.ERROR)

        milestones: list[dict] = loads(res.data)

        for milestone in milestones:
            if milestone['title'] == name:
                return GithubMilestone(milestone)

        # logs warning message since the passed milestone is not found.
        logging.warning(f'Milestone {name} was not found in repo {self.owner}/{self.repo}. url: {url}.')
        return None

    def create_issue(self, title: str, body: str, milestone: str = None, assignees: list[str] = None, labels: list[str] = None) -> GithubIssue:
        """ Creates an issue in the given repo.

        Args:
            title (str): Title of the issue.
            body (str): Body if the issue.
            milestone (str): Milestone name to be added to the issue.
            assignees (list[str]): List of usernames of  users that the issue has to be assigned.
            labels (list[str]): List of labels that has to be assigned to the issue.

        Returns: GithubIssue object 

        """

        url: str = f'https://api.github.com/repos/{self.owner}/{self.repo}/issues'
        if milestone is not None:
            milestone: GithubMilestone = self.get_milestone(name=milestone)
            payload: dict = {"title": title, "body": body, "milestone": milestone.number, "assignees": assignees, "labels": labels}
        else:
            payload = {"title": title, "body": body, "milestone": None, "assignees": assignees, "labels": labels}

        filtered = {k: v for k, v in payload.items() if v is not None}
        payload.clear()
        payload.update(filtered)

        res: Response = ResponseHandlers.curl_post_response(url=url, data=dumps(payload), headers=self._header)
        if res.status_code != 201:
            raise GithubApiException(msg='Unable to raise issue.', api='create_issue', response=res, error_type=ExceptionType.ERROR)

        return GithubIssue(data=res.data)


class GithubAppApi:
    """
    Methods to access Github App api endpoints.
    """
    _appId: str = None
    _time = int(round(datetime.now().timestamp()))
    payload: dict
    headers = CaseInsensitiveDict()
    exp_in_min: int = 5

    def __init__(self, app_id: str):
        """ Constructor
        """
        self._appId = app_id
        self.payload = {"iat": self._time, "exp": self._time + (60 * self.exp_in_min), "iss": app_id}
        self.headers["Accept"] = "application/vnd.github.v3+json"
        self.headers["Authorization"] = "Bearer " + generate_jwt_token(payload=self.payload)
        self.__internal_status = Status()

    def get_app_installations(self) -> list[GithubAppInstallations]:
        """
        Gets the app installations for the initialised app id

        :return: -> list[GithubAppInstallations]
        """
        _li: list[GithubAppInstallations] = []
        # endpoint url.
        url = "https://api.github.com/app/installations"

        res = ResponseHandlers.curl_get_response(url, self.headers)
        if res.status_code != 200:
            raise GithubAppApiException(msg='Couldn\'t get app installation', response=res, error_type=ExceptionType.ERROR, api='get_app_installations')

        _data: list = loads(res.data)
        for d in _data:
            _li.append(GithubAppInstallations(id=d['id'], org=d['account']['login'], tkn=d['access_tokens_url']))
        return _li

    def create_access_token(self, repos: list[str], org: str, permissions: AccessTokenPermission = None) -> GithubAccessToken:
        """
        Creates access tokens for the app installations to authenticate as an app in a repo

        Args:
            org (str): Organization for which the repos are present, this organization must have the App installed.
            repos (list[str]): List of repos for which the access token needs to be generated. *These repos must be from single organization*
            permissions (AccessTokenPermission): Permissions against which the access token needs to be generated. If nothing is passed then the default permissions assigned to the app will be assigned to the repos.
        """
        app_installations = enumerate(self.get_app_installations())
        __installation = None

        for count, installation in app_installations:
            if installation.org == org:
                __installation = installation
                break
            elif __installation is None and installation.org != org:
                raise GithubAppApiException(
                    msg=f'App not installed for the Org:{org}',
                    api='create_access_token',
                    response=Response(status_code=self.__internal_status.program_error['status'], status=self.__internal_status.program_error['msg'], data=f'{"message":"App not found for Org- {org}, so access token cannot be created."}'),
                    error_type=ExceptionType.WARNING
                )

        url = __installation.acc_tkn_url

        if permissions is None:
            payload: dict = {"repositories": repos}
        else:
            payload: dict = {"repositories": repos, "permissions": permissions.payload()}

        res = ResponseHandlers.curl_post_response(url=url, headers=self.headers, data=dumps(payload))
        if res.status_code != 201:
            raise GithubAppApiException(msg='Unable to create a access token', response=res, error_type=ExceptionType.ERROR, api='create_access_token')
        return GithubAccessToken(data=res.data)


if __name__ == '__main__':
    pass
