from enum import Enum

from lib.handlers import GithubAccessToken
from lib.handlers.response_handler import Response
from json import dumps


class Status(Enum):
    SUCCESS = 1
    FORBIDDEN = 2
    RES_NOT_FOUND = 3
    VAL_FAILED = 4
    NOT_FOUND = 5
    UNAUTHORIZED = 6


class GithubAPIMock:
    response: Response = None
    created: dict = {'status': 201, 'msg': 'Created'}
    success: dict = {'status': 200, 'msg': 'OK'}
    forbidden: dict = {'status': 403, 'msg': "Forbidden"}
    resNotFound: dict = {'status': 404, 'msg': 'Resource not found'}
    valFailed: dict = {'status': 422, 'msg': 'Validation Failed'}
    notFound: dict = {'status': 404, 'msg': 'NOT FOUND'}
    unauthorized: dict = {'status': 401, 'msg': 'Unauthorized'}
    for_status: Status

    def __init__(self, for_status: Status):
        self.for_status = for_status
        if self.for_status is Status.NOT_FOUND or self.for_status is None:
            self.response = Response(self.notFound['status'], self.notFound['msg'], '{"message": "Not Found", "documentation_url": "https://docs.github.com/rest/{endpoint}"}')
        else:
            st = self.status()
            self.response = Response(st['status'], st['msg'], '{"payload":"fail"}')

    def status(self) -> dict:
        """ Returns Status code and msg.
        Returns (dict): dict object of for_status code and msg

        """
        if self.for_status is Status.SUCCESS:
            return self.success
        elif self.for_status is Status.FORBIDDEN:
            return self.forbidden
        elif self.for_status is Status.RES_NOT_FOUND:
            return self.resNotFound
        elif self.for_status is Status.VAL_FAILED:
            return self.valFailed
        elif self.for_status is Status.NOT_FOUND:
            return self.notFound
        elif self.for_status is Status.UNAUTHORIZED:
            return self.unauthorized
        else:
            return self.notFound

    def post_blob(self) -> Response:
        if self.for_status is Status.SUCCESS:
            self.response.status_code = self.created['status']
            self.response.status = self.created['msg']
            self.response.data = dumps({
                "sha": "ecec23701aab1e48bce6323d9e149bdad4d2a879",
                "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/ecec23701aab1e48bce6323d9e149bdad4d2a879"
            })
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#create-a-blob"
            })
        elif self.for_status is Status.UNAUTHORIZED:
            self.response.data = dumps({
                "message": "Bad credentials",
                "documentation_url": "https://docs.github.com/rest"
            })
        else:
            self.response.data = '404: Not Found'

        return self.response

    def download_repo_file(self) -> Response:
        if self.for_status is Status.SUCCESS:
            self.response.data = "// This is a basic Flutter widget test.\n//\n// To perform an interaction with a widget in your test, use the WidgetTester\n// utility that Flutter provides. For example, you can send tap and scroll\n// gestures. You can also use WidgetTester to find child " \
                                 "widgets in the widget\n// tree, read text, and verify that the values of widget properties are correct.\n\nimport 'package:flutter/material.dart';\nimport 'package:flutter_test/flutter_test.dart';\n\nimport 'package:custom_card_design/main.dart';\n\nvoid main() {" \
                                 "\n  testWidgets('Counter increments smoke test', (WidgetTester tester) async {\n    // Build our app and trigger a frame.\n    await tester.pumpWidget(MyApp());\n\n    // Verify that our counter starts at 0.\n    expect(find.text('0'), " \
                                 "findsOneWidget);\n    expect(find.text('1'), findsNothing);\n\n    // Tap the '+' icon and trigger a frame.\n    await tester.tap(find.byIcon(Icons.add));\n    await tester.pump();\n\n    // Verify that our counter has incremented.\n    expect(find.text('0'), " \
                                 "findsNothing);\n    expect(find.text('1'), findsOneWidget);\n  });\n}\n"
        else:
            self.response.data = '404: Not Found'

        return self.response

    def getref(self) -> Response:
        """ Get Reference api response

        Returns (Response): A Response object

        """
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps({
                "ref": "refs/heads/test_branch",
                "node_id": "REF_kwDOG0SbL7ZyZWZzL2hlYWRzL3Rlc3RfYnJhbmNo",
                "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch",
                "object": {
                    "sha": "4a162230020ca9adb70c809f5a40a8ba3551dce2",
                    "type": "commit",
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/4a162230020ca9adb70c809f5a40a8ba3551dce2"
                }
            })
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#get-a-reference"
            })
        return self.response

    def get_commit(self) -> Response:
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps({
                "sha": "4a162230020ca9adb70c809f5a40a8ba3551dce2",
                "node_id": "C_kwDOG0SbL9oAKDRhMTYyMjMwMDIwY2E5YWRiNzBjODA5ZjVhNDBhOGJhMzU1MWRjZTI",
                "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/4a162230020ca9adb70c809f5a40a8ba3551dce2",
                "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/4a162230020ca9adb70c809f5a40a8ba3551dce2",
                "author": {
                    "name": "aatmaram-bhide-bot[bot]",
                    "email": "100037318+aatmaram-bhide-bot[bot]@users.noreply.github.com",
                    "date": "2022-03-02T17:07:32Z"
                },
                "committer": {
                    "name": "GitHub",
                    "email": "noreply@github.com",
                    "date": "2022-03-02T17:07:32Z"
                },
                "tree": {
                    "sha": "47b01c17a28529cd72f150f403022fc46d061452",
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/47b01c17a28529cd72f150f403022fc46d061452"
                },
                "message": "New commit",
                "parents": [
                    {
                        "sha": "c2675d3104aeacc81a155f4cbfe54b0615e70f32",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/c2675d3104aeacc81a155f4cbfe54b0615e70f32",
                        "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/c2675d3104aeacc81a155f4cbfe54b0615e70f32"
                    }
                ],
                "verification": {
                    "verified": True,
                    "reason": "valid",
                    "signature": "-----BEGIN PGP SIGNATURE-----\n\n{signature}\n\n-----END PGP SIGNATURE-----\n",
                    "payload": "tree 47b01c17a28529cd72f150f403022fc46d061452\nparent c2675d3104aeacc81a155f4cbfe54b0615e70f32\nauthor aatmaram-bhide-bot[bot] <100037318+aatmaram-bhide-bot[bot]@users.noreply.github.com> 1646240852 +0000\ncommitter GitHub <noreply@github.com> 1646240852 "
                               "+0000\n\nNew commit "
                }
            })
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#get-a-reference"
            })
        return self.response

    def get_tree(self, recursive: bool = True):
        if self.for_status is Status.SUCCESS and recursive is True:
            self.response.data = dumps({
                "sha": "47b01c17a28529cd72f150f403022fc46d061452",
                "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/47b01c17a28529cd72f150f403022fc46d061452",
                "tree": [
                    {
                        "path": ".circleci",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "4aa50b2cb143654823f1f81c68a0d0deb06e8c80",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/4aa50b2cb143654823f1f81c68a0d0deb06e8c80"
                    },
                    {
                        "path": ".circleci/config.yml",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "6f98693addd5cba9a40f6ab9335054951a78b2ee",
                        "size": 449,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/6f98693addd5cba9a40f6ab9335054951a78b2ee"
                    },
                    {
                        "path": ".github",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "5df41bac369a0132c47d81af980366628c40d15f",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/5df41bac369a0132c47d81af980366628c40d15f"
                    },
                    {
                        "path": ".github/labeler.yml",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "e8c1cc94aa60d90fe331a285605c12ace07f58fc",
                        "size": 493,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/e8c1cc94aa60d90fe331a285605c12ace07f58fc"
                    },
                    {
                        "path": ".github/workflows",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "b6fa3f4354e24c2cfec37a4b5d929744f84bb0c0",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/b6fa3f4354e24c2cfec37a4b5d929744f84bb0c0"
                    },
                    {
                        "path": ".github/workflows/label.yml",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "a3cad4323df1362e1c5caf1ca192fd36d1ba64aa",
                        "size": 498,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/a3cad4323df1362e1c5caf1ca192fd36d1ba64aa"
                    },
                    {
                        "path": ".gitignore",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "dbef116d224d8f796abe72ecfef9271f9d79f069",
                        "size": 618,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/dbef116d224d8f796abe72ecfef9271f9d79f069"
                    },
                    {
                        "path": "LICENSE",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "82eba2f8c0d4a00bf67deb72a68ecfcff29f68ff",
                        "size": 1521,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/82eba2f8c0d4a00bf67deb72a68ecfcff29f68ff"
                    },
                    {
                        "path": "README.md",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "e36ecc3cb45958b71efbd968723a4d346d5241f0",
                        "size": 305,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/e36ecc3cb45958b71efbd968723a4d346d5241f0"
                    },
                    {
                        "path": "custom_card_design",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "4e01a14f50c83d758c107d4a4d752bbdd073552b",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/4e01a14f50c83d758c107d4a4d752bbdd073552b"
                    },
                    {
                        "path": "custom_card_design/.gitignore",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "f3c205341e7dbb11f1dfecee67a1cd1f84660a22",
                        "size": 722,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/f3c205341e7dbb11f1dfecee67a1cd1f84660a22"
                    },
                    {
                        "path": "custom_card_design/README.md",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "373ad06e12baffe6261944e80a8e79178117a015",
                        "size": 507,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/373ad06e12baffe6261944e80a8e79178117a015"
                    },
                    {
                        "path": "custom_card_design/lib",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "ccc0316b0f7da00a02eeb4c696119b1e8eeb3c88",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/ccc0316b0f7da00a02eeb4c696119b1e8eeb3c88"
                    },
                    {
                        "path": "custom_card_design/lib/main.dart",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "60f4891b28608fe03cdd544fd7fdb77c00e34675",
                        "size": 3883,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/60f4891b28608fe03cdd544fd7fdb77c00e34675"
                    },
                    {
                        "path": "custom_card_design/lib/sunflower.dart",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "7616871141cc1b313bfd92271df48e505d29eb31",
                        "size": 4011,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/7616871141cc1b313bfd92271df48e505d29eb31"
                    },
                    {
                        "path": "custom_card_design/test",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "ab36ed17e98f0262b2bdad181c2f6168293168b6",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/ab36ed17e98f0262b2bdad181c2f6168293168b6"
                    },
                    {
                        "path": "custom_card_design/test/change_file_test.txt",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "e42afe058b5f88127000a4406a059b06694a3c4f",
                        "size": 1051,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/e42afe058b5f88127000a4406a059b06694a3c4f"
                    },
                    {
                        "path": "custom_card_design/test/widget_test.dart",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "e7a083314c93505805d26f97851a6ceedf902524",
                        "size": 1057,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/e7a083314c93505805d26f97851a6ceedf902524"
                    }
                ],
                "truncated": False
            })
        elif self.for_status == Status.SUCCESS:
            self.response.data = dumps({
                "sha": "47b01c17a28529cd72f150f403022fc46d061452",
                "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/47b01c17a28529cd72f150f403022fc46d061452",
                "tree": [
                    {
                        "path": ".circleci",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "4aa50b2cb143654823f1f81c68a0d0deb06e8c80",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/4aa50b2cb143654823f1f81c68a0d0deb06e8c80"
                    },
                    {
                        "path": ".github",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "5df41bac369a0132c47d81af980366628c40d15f",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/5df41bac369a0132c47d81af980366628c40d15f"
                    },
                    {
                        "path": ".gitignore",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "dbef116d224d8f796abe72ecfef9271f9d79f069",
                        "size": 618,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/dbef116d224d8f796abe72ecfef9271f9d79f069"
                    },
                    {
                        "path": "LICENSE",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "82eba2f8c0d4a00bf67deb72a68ecfcff29f68ff",
                        "size": 1521,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/82eba2f8c0d4a00bf67deb72a68ecfcff29f68ff"
                    },
                    {
                        "path": "README.md",
                        "mode": "100644",
                        "type": "blob",
                        "sha": "e36ecc3cb45958b71efbd968723a4d346d5241f0",
                        "size": 305,
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/e36ecc3cb45958b71efbd968723a4d346d5241f0"
                    },
                    {
                        "path": "custom_card_design",
                        "mode": "040000",
                        "type": "tree",
                        "sha": "4e01a14f50c83d758c107d4a4d752bbdd073552b",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/4e01a14f50c83d758c107d4a4d752bbdd073552b"
                    }
                ],
                "truncated": False
            })
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#get-a-tree"
            })

        return self.response

    def create_access_token(self) -> GithubAccessToken:
        mock_reponse = {
            "token": "ghs_4e2p8GfZojm90SMqvs8f8QEi1qYQLb1WOysw",
            "expires_at": "2022-03-25T16:52:52Z",
            "permissions": {
                "members": "read",
                "actions": "read",
                "contents": "write",
                "issues": "write",
                "metadata": "read",
                "pull_requests": "write",
                "workflows": "write"
            },
            "repository_selection": "selected",
            "repositories": [{
                "id": 457481007,
                "node_id": "R_kgDOG0SbLw",
                "name": "fuzzy-train",
                "full_name": "Coders-Asylum/fuzzy-train",
                "private": False,
                "owner": {
                    "login": "Coders-Asylum",
                    "id": 58622402,
                    "node_id": "MDEyOk9yZ2FuaXphdGlvbjU4NjIyNDAy",
                    "avatar_url": "https://avatars.githubusercontent.com/u/58622402?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/Coders-Asylum",
                    "html_url": "https://github.com/Coders-Asylum",
                    "followers_url": "https://api.github.com/users/Coders-Asylum/followers",
                    "following_url": "https://api.github.com/users/Coders-Asylum/following{/other_user}",
                    "gists_url": "https://api.github.com/users/Coders-Asylum/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/Coders-Asylum/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/Coders-Asylum/subscriptions",
                    "organizations_url": "https://api.github.com/users/Coders-Asylum/orgs",
                    "repos_url": "https://api.github.com/users/Coders-Asylum/repos",
                    "events_url": "https://api.github.com/users/Coders-Asylum/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/Coders-Asylum/received_events",
                    "type": "Organization",
                    "site_admin": False
                },
                "html_url": "https://github.com/Coders-Asylum/fuzzy-train",
                "description": "Sandbox environment for testing integrations and apps",
                "fork": False,
                "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train",
                "forks_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/forks",
                "keys_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/teams",
                "hooks_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/hooks",
                "issue_events_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/issues/events{/number}",
                "events_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/events",
                "assignees_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/assignees{/user}",
                "branches_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/branches{/branch}",
                "tags_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/tags",
                "blobs_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/languages",
                "stargazers_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/stargazers",
                "contributors_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contributors",
                "subscribers_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/subscribers",
                "subscription_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/subscription",
                "commits_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contents/{+path}",
                "compare_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/merges",
                "archive_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/downloads",
                "issues_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/issues{/number}",
                "pulls_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/labels{/name}",
                "releases_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/releases{/id}",
                "deployments_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/deployments",
                "created_at": "2022-02-09T18:29:09Z",
                "updated_at": "2022-02-23T10:50:00Z",
                "pushed_at": "2022-03-02T17:07:32Z",
                "git_url": "git://github.com/Coders-Asylum/fuzzy-train.git",
                "ssh_url": "git@github.com:Coders-Asylum/fuzzy-train.git",
                "clone_url": "https://github.com/Coders-Asylum/fuzzy-train.git",
                "svn_url": "https://github.com/Coders-Asylum/fuzzy-train",
                "homepage": None,
                "size": 71,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": "Dart",
                "has_issues": True,
                "has_projects": True,
                "has_downloads": True,
                "has_wiki": True,
                "has_pages": True,
                "forks_count": 0,
                "mirror_url": None,
                "archived": False,
                "disabled": False,
                "open_issues_count": 0,
                "license": {
                    "key": "bsd-3-clause",
                    "name": "BSD 3-Clause \"New\" or \"Revised\" License",
                    "spdx_id": "BSD-3-Clause",
                    "url": "https://api.github.com/licenses/bsd-3-clause",
                    "node_id": "MDc6TGljZW5zZTU="
                },
                "allow_forking": True,
                "is_template": False,
                "topics": ["sandbox", "testing-tool"],
                "visibility": "public",
                "forks": 0,
                "open_issues": 0,
                "watchers": 0,
                "default_branch": "main"
            }]
        }

        if self.for_status is Status.SUCCESS:
            return GithubAccessToken(data=dumps(mock_reponse))

    def get_latest_release(self, latest: bool = True) -> Response:
        if self.for_status is Status.SUCCESS and latest is True:
            self.response.data = dumps(
                {
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/releases/62842233",
                    "assets_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/releases/62842233/assets",
                    "upload_url": "https://uploads.github.com/repos/Coders-Asylum/fuzzy-train/releases/62842233/assets{?name,label}",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/releases/tag/V0.0.1a",
                    "id": 62842233,
                    "author": {
                        "login": "Maverick099",
                        "id": 32545664,
                        "node_id": "MDQ6VXNlcjMyNTQ1NjY0",
                        "avatar_url": "https://avatars.githubusercontent.com/u/32545664?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/Maverick099",
                        "html_url": "https://github.com/Maverick099",
                        "followers_url": "https://api.github.com/users/Maverick099/followers",
                        "following_url": "https://api.github.com/users/Maverick099/following{/other_user}",
                        "gists_url": "https://api.github.com/users/Maverick099/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/Maverick099/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/Maverick099/subscriptions",
                        "organizations_url": "https://api.github.com/users/Maverick099/orgs",
                        "repos_url": "https://api.github.com/users/Maverick099/repos",
                        "events_url": "https://api.github.com/users/Maverick099/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/Maverick099/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "node_id": "RE_kwDOG0SbL84DvuV5",
                    "tag_name": "V0.0.1a",
                    "target_commitish": "main",
                    "name": "V0.0.1a",
                    "draft": False,
                    "prerelease": False,
                    "created_at": "2022-02-13T09:55:05Z",
                    "published_at": "2022-03-26T14:44:33Z",
                    "assets": [],
                    "tarball_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/tarball/V0.0.1a",
                    "zipball_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/zipball/V0.0.1a",
                    "body": "## What's Changed\r\n* Delete .idea directory (#1) by @Maverick099 in https://github.com/Coders-Asylum/fuzzy-train/pull/2\r\n* Added caution statements by @Maverick099 in https://github.com/Coders-Asylum/fuzzy-train/pull/3\r\n* Forward merge by @Maverick099 in "
                            "https://github.com/Coders-Asylum/fuzzy-train/pull/5\r\n\r\n\r\n**Full Changelog**: https://github.com/Coders-Asylum/fuzzy-train/commits/V0.0.1a",
                    "mentions_count": 1
                })
        elif self.for_status is Status.SUCCESS and latest is False:
            self.response.data = dumps(
                [
                    {
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/releases/62842233",
                        "assets_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/releases/62842233/assets",
                        "upload_url": "https://uploads.github.com/repos/Coders-Asylum/fuzzy-train/releases/62842233/assets{?name,label}",
                        "html_url": "https://github.com/Coders-Asylum/fuzzy-train/releases/tag/V0.0.1a",
                        "id": 62842233,
                        "author": {
                            "login": "Maverick099",
                            "id": 32545664,
                            "node_id": "MDQ6VXNlcjMyNTQ1NjY0",
                            "avatar_url": "https://avatars.githubusercontent.com/u/32545664?v=4",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/Maverick099",
                            "html_url": "https://github.com/Maverick099",
                            "followers_url": "https://api.github.com/users/Maverick099/followers",
                            "following_url": "https://api.github.com/users/Maverick099/following{/other_user}",
                            "gists_url": "https://api.github.com/users/Maverick099/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/Maverick099/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/Maverick099/subscriptions",
                            "organizations_url": "https://api.github.com/users/Maverick099/orgs",
                            "repos_url": "https://api.github.com/users/Maverick099/repos",
                            "events_url": "https://api.github.com/users/Maverick099/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/Maverick099/received_events",
                            "type": "User",
                            "site_admin": False
                        },
                        "node_id": "RE_kwDOG0SbL84DvuV5",
                        "tag_name": "V0.0.1a",
                        "target_commitish": "main",
                        "name": "V0.0.1a",
                        "draft": False,
                        "prerelease": False,
                        "created_at": "2022-02-13T09:55:05Z",
                        "published_at": "2022-03-26T14:44:33Z",
                        "assets": [],
                        "tarball_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/tarball/V0.0.1a",
                        "zipball_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/zipball/V0.0.1a",
                        "body": "## What's Changed\r\n* Delete .idea directory (#1) by @Maverick099 in https://github.com/Coders-Asylum/fuzzy-train/pull/2\r\n* Added caution statements by @Maverick099 in https://github.com/Coders-Asylum/fuzzy-train/pull/3\r\n* Forward merge by @Maverick099 in "
                                "https://github.com/Coders-Asylum/fuzzy-train/pull/5\r\n\r\n\r\n**Full Changelog**: https://github.com/Coders-Asylum/fuzzy-train/commits/V0.0.1a",
                        "mentions_count": 1
                    }
                ])
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/repos#list-releases"
                }
            )

        return self.response

    def trigger_workflow(self) -> Response:
        if self.for_status is Status.SUCCESS:
            self.response.status_code = 204
            self.response.status = 'No Content'
            self.response.data = ''
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/actions#create-a-workflow-dispatch-event"
            })
            return self.response
        elif self.for_status is Status.UNAUTHORIZED:
            self.response.data = dumps(
                {
                    "message": "Bad credentials",
                    "documentation_url": "https://docs.github.com/rest"
                })

        return self.response

    def get_tag(self):
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps(
                [
                    {
                        "name": "V0.0.1a",
                        "zipball_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/zipball/refs/tags/V0.0.1a",
                        "tarball_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/tarball/refs/tags/V0.0.1a",
                        "commit": {
                            "sha": "1f079f4effdde3b001991d6707b92d846f0d398a",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/1f079f4effdde3b001991d6707b92d846f0d398a"
                        },
                        "node_id": "REF_kwDOG0SbL7FyZWZzL3RhZ3MvVjAuMC4xYQ"
                    }
                ])
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/repos#list-repository-tags"
                })

        return self.response
