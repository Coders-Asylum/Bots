from lib.handlers.response_handler import ResponseHandlers, Response
from lib.handlers.authHandler import generate_jwt_token
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from json import loads, dumps
from enum import Enum


class GithubBlob:
    url: str
    sha: str

    def __init__(self, data: str = None):
        _j = loads(data)
        self.url = _j['url']
        self.sha = _j['sha']


class GithubRefObject:
    ref: str
    nodeId: str
    url: str
    obj: dict

    def __init__(self, data: str):
        _j = loads(data)
        self.ref = _j['ref']
        self.nodeId = _j['node_id']
        self.url = _j['url']
        self.obj = _j['object']


class GithubCommitObject:
    sha: str
    author: dict
    committer: dict
    message: str
    tree: dict

    def __init__(self, data: str):
        _j = loads(data)
        self.sha = _j['sha']
        self.author = _j['author']
        self.committer = _j['committer']
        self.message = _j['message']
        self.tree = _j['tree']


class GithubTreeObject:
    sha: str
    url: str
    tree: list[dict]

    def __init__(self, data: str):
        _j = loads(data)
        self.sha = _j['sha']
        self.url = _j['url']
        self.tree = _j['tree']


class TreeType(Enum):
    BLOB = '100644'
    EXECUTABLE = '100755'
    TREE = '040000'
    COMMIT = '160000'
    SYMLINK = '120000'


class GitTree:
    path: str
    mode: str
    type: str
    sha: str
    content: str
    type: dict = {'100644': 'blob', '100755': 'blob', '040000': 'tree', '160000': 'commit', '120000': 'blob'}

    def __init__(self, path: str, tree_type: TreeType, sha: str = None, content: str = None, delete: bool = False):
        assert sha is None or content is None, 'SHA or Content must specified, specifying both will cause error'
        self.path = path
        self.mode = tree_type.value
        self.type = self.type[tree_type.value]

        # If the file needs to be deleted.
        # todo: add lines to check if the file is present in the fetched tree only then delete else ignore and fill log as a warning and print the warning.
        if delete is True:
            self.content = 'delete'
            self.sha = 'delete'
        else:
            self.content = content
            self.sha = sha


class GithubAppInstallations:
    org: str
    install_id: int
    acc_tkn_url: str

    def __init__(self, org: str, id: int, tkn: str):
        self.org = org
        self.install_id = id
        self.acc_tkn_url = tkn

    def __str__(self):
        _s: str = f'Installed on: Organization: {self.org}, Installation id: {self.install_id}'
        return _s


class AccessType(Enum):
    """Type of access need for the permission

    Attributes
    ----------
    READ : Give read access for the permission
    WRITE: Give write access.
    NULL : No access against the permission

    """
    READ = "read"
    WRITE = "write"
    NULL = "NULL"


class Permission:
    name: str
    access_type: AccessType

    def __init__(self, name: str, access_type: AccessType):
        self.name = name
        self.access_type = access_type


class GithubPermissions(Enum):
    """
    These are the permissions that are available in `properties for permission parameter <https://docs.github.com/en/rest/reference/apps#create-an-installation-access-token-for-an-app--parameters>`
       To know about the permission look in to this part of the `Github api <https://docs.github.com/en/rest/reference/permissions-required-for-github-apps>`

       Note: Add the permission to the following class if not found in the class but is available in the Github APP api docs.
    """

    CONTENTS = 'contents'
    ISSUES = 'issues'
    PAGES = 'pages'
    PULL_REQUESTS = 'pull_requests'
    MEMBERS = 'members'


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
    @staticmethod
    def download_repo_file(repo_name: str, owner: str, file_path: str, branch: str = 'master'):
        """ Downloads file from GitHub repository
        :param repo_name: Name of repository where the file is located
        :param owner: Name of organization or User of the repository
        :param file_path: path of the file from the home root directory with / and file extension as it is
        :param branch: Repository branch from which the file must be fetched, is defaulted to 'master'
        :return: File contents as string
        """
        url: str = f'https://raw.githubusercontent.com/{owner}/{repo_name}/{branch}/{file_path}'
        _r: Response = ResponseHandlers.http_get_response(url)
        return _r

    @staticmethod
    def get_git_ref(owner: str, repo_name: str, branch_name: str):
        """
        Gets the Git head reference of the branch specified
        :param owner:
        :param repo_name:
        :param branch_name:
        :return: --> GithubRefObject
        """
        _url: str = f'https://api.github.com/repos/{owner}/{repo_name}/git/ref/heads/{branch_name}'
        _header: CaseInsensitiveDict = CaseInsensitiveDict()
        _header['Accept'] = 'application/vnd.github.v3+json'

        _r: Response = ResponseHandlers.curl_get_response(url=_url, headers=_header)
        if _r.status_code != 200:
            print(f'Error in fetching data: {_r.status_code} {_r.status}')
        return GithubRefObject(data=_r.data)

    @staticmethod
    def post_blob(owner: str, repo: str, data: str):
        url: str = f'https://api.github.com/repos/{owner}/{repo}/git/blobs/'
        _header: CaseInsensitiveDict = CaseInsensitiveDict()
        _header['Accept'] = 'application/vnd.github.v3+json'
        _data: str = dumps({"content": data})
        print(url)
        _r: Response = ResponseHandlers.curl_post_response(url=url, headers=_header, data=_data)
        if _r.status_code != 201:
            print(f'Blog not posted: {_r.status_code} {_r.status}')

        return GithubBlob(data=_r.data)

    @staticmethod
    def get_latest_commit(owner: str, repo: str, branch: str):
        _ref: GithubRefObject = GithubAPIHandler.get_git_ref(owner=owner, repo_name=repo, branch_name=branch)
        _header: CaseInsensitiveDict = CaseInsensitiveDict()
        _header['Accept'] = 'application/vnd.github.v3+json'

        # get and store the commit object
        _r: Response = ResponseHandlers.curl_get_response(url=_ref.obj['url'], headers=_header)
        if _r.status_code != 200:
            print('Error: was not able to get commit object')
        return GithubCommitObject(data=_r.data)

    @staticmethod
    def get_tree(owner: str, repo: str, branch: str):
        _header: CaseInsensitiveDict = CaseInsensitiveDict()
        _header['Accept'] = 'application/vnd.github.v3+json'

        _commit: GithubCommitObject = GithubAPIHandler.get_latest_commit(owner=owner, repo=repo, branch=branch)

        # get the tree and return the tree
        # recursive=1 at the end of the tree url helps to get tree objects for all the files with any depth in the repo.
        _r = ResponseHandlers.curl_get_response(url=_commit.tree['url'] + '?recursive=1', headers=_header)
        if _r.status_code != 200:
            print('Error: was not able to get tree object')
        return GithubTreeObject(data=_r.data)

    @staticmethod
    def update_and_post_tree(owner: str, repo: str, branch: str, files: list[GitTree]):
        """
        Updates the tree according to files provided
        :param owner:
        :param repo:
        :param branch:
        :param files:
        :return:
        """
        _header: CaseInsensitiveDict = CaseInsensitiveDict()
        _header['Accept'] = 'application/vnd.github.v3+json'

        # api url
        url = f'https://api.github.com/repos/{owner}/{repo}/git/trees'

        _git_tree: GithubTreeObject = GithubAPIHandler.get_tree(owner=owner, repo=repo, branch=branch)

        #  checking for updated files.
        c: int = 0
        for file in files:
            for tree in _git_tree.tree:
                if file.path is tree['path']:
                    tree['mode'] = file.mode
                    tree['type'] = file.type
                    if file.content is None:
                        tree['sha'] = file.sha
                    else:
                        tree.pop('sha')
                        tree['content'] = file.content
                    files.pop(c)
                else:
                    pass
            c = +1

            # if still files are remaining this will add them as a new files.
            if len(files) != 0:
                for f in files:
                    tree: dict
                    if f.content and f.sha == 'delete':
                        tree = {"path": f.path, "mode": f.mode, "type": f.type}
                    elif f.content is None:
                        tree = {"path": f.path, "mode": f.mode, "type": f.type, "sha": f.sha}
                    else:
                        tree = {"path": f.path, "mode": f.mode, "type": f.type, "content": f.content}
                    _git_tree.tree.append(tree)
            else:
                pass

        _res = ResponseHandlers.curl_post_response(url=url, headers=_header, data=dumps(_git_tree.tree))
        if _res.status_code != 201:
            print(f'Tree was not able to be updated because: {_res.status_code} {_res.status}')

        print(_res.data)

        return GithubTreeObject(data=_res.data)

    @staticmethod
    def commit_files(owner: str, repo: str, branch: str, files: list[GitTree]):
        pass


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
        self._appId = app_id
        self.payload = {"iat": self._time, "exp": self._time + (60 * self.exp_in_min), "iss": app_id}
        self.headers["Accept"] = "application/vnd.github.v3+json"
        self.headers["Authorization"] = "Bearer " + generate_jwt_token(payload=self.payload)

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
            print(f'App installation was not received: {res.status_code} {res.status} {res.data}')

        _data: list = loads(res.data)
        for d in _data:
            _li.append(GithubAppInstallations(id=d['id'], org=d['account']['login'], tkn=d['access_tokens_url']))
        return _li

    def create_access_token(self, repos: list[str], permissions: AccessTokenPermission, org: str):
        """
        Creates access tokens for the app installations to authenticate as an app in a repo

        Args:
            org (str): Organization for which the repos are present, this organization must have the App installed.
            repos (list[str]): List of repos for which the access token needs to be generated. *These repos must be from single organization*
            permissions (AccessTokenPermission): Permissions against which the access token needs to be generated. If nothing is passed then the default permissions assigned to the app will be assigned to the repos.
        """
        app_installations = self.get_app_installations()
        _index: int = 10000001
        for i in range(len(app_installations)):
            if app_installations[i].org == org:
                _index = i
                break
            elif i == len(app_installations) - 1 and app_installations[i].org != org:
                raise Exception(f'App not installed for the Org:{org}')

        url = app_installations[_index].acc_tkn_url

        if permissions is None:
            payload: dict = {"repositories": repos}
        else:
            payload: dict = {"repositories": repos, "permissions": permissions.payload()}

        res = ResponseHandlers.curl_post_response(url=url, headers=self.headers, data=dumps(payload))
        if res.status_code != 201:
            print(f'[E] Token was not created: {res.status_code} {res.status}: {res.data}')
        print(res.status)


if __name__ == '__main__':
    app = GithubAppApi(app_id='173901')
    access_tkn1: AccessTokenPermission = AccessTokenPermission()

    access_tkn1.set(permission=GithubPermissions.CONTENTS, access=AccessType.READ)

    app.create_access_token(repos=['fuzzy-train'], permissions=access_tkn1, org='Coders-Asylum')
