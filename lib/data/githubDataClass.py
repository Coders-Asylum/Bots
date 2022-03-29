from enum import Enum
from json import loads


class Repository:
    owner: str
    name: str
    branch: str
    map: dict

    def __init__(self, owner: str, repo: str, branch: str):
        self.owner = owner
        self.name = repo
        self.branch = branch
        self.map = {"owner": owner, "name": repo, "branch": branch}

    def __getitem__(self, item: str):
        return self.map[item]


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


class GithubRelease:
    tag: str
    pre_release: bool
    node_id: str

    def __init__(self, data: str):
        j = loads(data)
        self.tag = j['tag_name']
        self.pre_release = j['prerelease']
        self.node_id = j['node_id']
