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

    def get_latest_ref(self) -> Response:
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps(
                {
                    "ref": "refs/heads/test_branch",
                    "node_id": "REF_kwDOG0SbL7ZyZWZzL2hlYWRzL3Rlc3RfYnJhbmNo",
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch",
                    "object": {
                        "sha": "c30dbe34699b8e7e522885bc9d2a4d9d141c9382",
                        "type": "commit",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/c30dbe34699b8e7e522885bc9d2a4d9d141c9382"
                    }
                })
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#get-a-reference"
            })
        return self.response

    def get_git_commit(self):
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps(
                {
                    "sha": "c30dbe34699b8e7e522885bc9d2a4d9d141c9382",
                    "node_id": "C_kwDOG0SbL9oAKGMzMGRiZTM0Njk5YjhlN2U1MjI4ODViYzlkMmE0ZDlkMTQxYzkzODI",
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/c30dbe34699b8e7e522885bc9d2a4d9d141c9382",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/c30dbe34699b8e7e522885bc9d2a4d9d141c9382",
                    "author": {
                        "name": "aatmaram-bhide-bot[bot]",
                        "email": "100037318+aatmaram-bhide-bot[bot]@users.noreply.github.com",
                        "date": "2022-04-05T17:10:44Z"
                    },
                    "committer": {
                        "name": "GitHub",
                        "email": "noreply@github.com",
                        "date": "2022-04-05T17:10:44Z"
                    },
                    "tree": {
                        "sha": "47b01c17a28529cd72f150f403022fc46d061452",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/47b01c17a28529cd72f150f403022fc46d061452"
                    },
                    "message": "New test file",
                    "parents": [
                        {
                            "sha": "aa8052742b140c8403925dd574dbc045bafcd028",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/aa8052742b140c8403925dd574dbc045bafcd028",
                            "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/aa8052742b140c8403925dd574dbc045bafcd028"
                        }
                    ],
                    "verification": {
                        "verified": True,
                        "reason": "valid",
                        "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiTHgUCRBK7hj4Ov3rIwAAPAQIADoblAf29cBFjFG2wdCnYKLD\nQK5zI7UWSqVXRJaGop15w1Wioh/EMZm0TT1b82socKd17akeCRxeaZI1Yr1IQ5r6\n7zqq6vHvlTTt+QJpw93WADglvK73js7bzJoU4giIGbKpXIVAfBixYtSi1k84g0Dc"
                                     "\nTRPgIRsEF7HUQqhVv3UjpQ9krSc1iqOWlz4Hm6tu7Wzf8q/Z+myrYdZxtZkchmQg\nPAL5EzVWzWVc4BSrR9In8PByCN+kFYrUmeYYnKHal5IMbVtSvUFKT0c5jWQ6vMNZ\n1gwF9M3q0sOPHoa/UI+spwj317VKZGzNFnjhRn7B3ritk4DRk+0hvJkM3qAnbl0=\n=4aBk\n-----END PGP SIGNATURE-----\n",
                        "payload": "tree 47b01c17a28529cd72f150f403022fc46d061452\nparent aa8052742b140c8403925dd574dbc045bafcd028\nauthor aatmaram-bhide-bot[bot] <100037318+aatmaram-bhide-bot[bot]@users.noreply.github.com> 1649178644 +0000\ncommitter GitHub <noreply@github.com> 1649178644 "
                                   "+0000\n\nNew test file "
                    }
                }
            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#get-a-reference"
            })
        return self.response

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

    def get_git_tree(self, recursive: bool = True):
        if self.for_status is Status.SUCCESS and recursive is True:
            self.response.data = dumps(
                {
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
                }
            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps({
                "message": "Not Found",
                "documentation_url": "https://docs.github.com/rest/reference/git#get-a-tree"
            })
        return self.response

    def post_git_tree(self):
        if self.for_status is Status.SUCCESS:
            self.response.status_code = self.created['status']
            self.response.status = self.created['msg']
            self.response.data = dumps(
                {"sha": "47b01c17a28529cd72f150f403022fc46d061452", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/47b01c17a28529cd72f150f403022fc46d061452",
                 "tree": [{"path": ".circleci", "mode": "040000", "type": "tree", "sha": "4aa50b2cb143654823f1f81c68a0d0deb06e8c80", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/4aa50b2cb143654823f1f81c68a0d0deb06e8c80"},
                          {"path": ".github", "mode": "040000", "type": "tree", "sha": "5df41bac369a0132c47d81af980366628c40d15f", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/5df41bac369a0132c47d81af980366628c40d15f"},
                          {"path": ".gitignore", "mode": "100644", "type": "blob", "sha": "dbef116d224d8f796abe72ecfef9271f9d79f069", "size": 618, "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/dbef116d224d8f796abe72ecfef9271f9d79f069"},
                          {"path": "LICENSE", "mode": "100644", "type": "blob", "sha": "82eba2f8c0d4a00bf67deb72a68ecfcff29f68ff", "size": 1521, "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/82eba2f8c0d4a00bf67deb72a68ecfcff29f68ff"},
                          {"path": "README.md", "mode": "100644", "type": "blob", "sha": "e36ecc3cb45958b71efbd968723a4d346d5241f0", "size": 305, "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/blobs/e36ecc3cb45958b71efbd968723a4d346d5241f0"},
                          {"path": "custom_card_design", "mode": "040000", "type": "tree", "sha": "4e01a14f50c83d758c107d4a4d752bbdd073552b", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/4e01a14f50c83d758c107d4a4d752bbdd073552b"}], "truncated": False
                 }
            )
        elif self.for_status is Status.UNAUTHORIZED:
            self.response.data = dumps({
                "message": "Bad credentials",
                "documentation_url": "https://docs.github.com/rest"
            })
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/git#create-a-tree"
                }
            )
        else:
            self.response.data = '404: Not Found'
        return self.response

    def post_git_commit(self):
        self.response.status_code = self.created['status']
        self.response.status = self.created['msg']
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps(
                {
                    "sha": "7f0624ce1d9407aecae6e38dd007dea0265b12c2", "node_id": "C_kwDOG0SbL9oAKDdmMDYyNGNlMWQ5NDA3YWVjYWU2ZTM4ZGQwMDdkZWEwMjY1YjEyYzI", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/7f0624ce1d9407aecae6e38dd007dea0265b12c2",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/7f0624ce1d9407aecae6e38dd007dea0265b12c2", "author": {"name": "aatmaram-bhide-bot[bot]", "email": "100037318+aatmaram-bhide-bot[bot]@users.noreply.github.com", "date": "2022-04-06T18:21:33Z"},
                    "committer": {
                        "name": "GitHub",
                        "email": "noreply@github.com",
                        "date": "2022-04-06T18:21:33Z"
                    },
                    "tree": {"sha": "47b01c17a28529cd72f150f403022fc46d061452", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/47b01c17a28529cd72f150f403022fc46d061452"},
                    "message": "New test file",
                    "parents": [
                        {
                            "sha": "c30dbe34699b8e7e522885bc9d2a4d9d141c9382", "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/c30dbe34699b8e7e522885bc9d2a4d9d141c9382",
                            "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/c30dbe34699b8e7e522885bc9d2a4d9d141c9382"
                        }
                    ],
                    "verification": {
                        "verified": True, "reason": "valid",
                        "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiTdotCRBK7hj4Ov3rIwAAql4IAGJgFLtu6r9oogox/kV6ujV3\npl02HM3osNan6kgvjt/bC7nYUeycoapAKNMB91s2/7J7ZjETy8L9sV+Em7WNvobk\njdAEytQK8WdLDtg//p3PUWUh/csRY5QPc3zC7rl7RwS+6tCvppWqyUrx1B3Bvzh"
                                     "+\n56By2IwH34EO1oJo2xkXex4dQHc3/Sy6ImMPIA4Sg9BuAEEncSj5hvG+nRr9UMR4\nbIZ1bWDrJ+owH62v/QmP0eptdOrfhruHOlGRayDy/aqGiqPu9zhlM+wzMiSukff8\n0+PszRU+5SWGk11wc2wx8fFq6FQ7MHteLiSWS1Tp3cbLcp48A8t6yqkWvS8tT5I=\n=RULJ\n-----END PGP SIGNATURE-----\n",
                        "payload": "tree 47b01c17a28529cd72f150f403022fc46d061452\nparent c30dbe34699b8e7e522885bc9d2a4d9d141c9382\nauthor aatmaram-bhide-bot[bot] <100037318+aatmaram-bhide-bot[bot]@users.noreply.github.com> 1649269293 +0000\ncommitter GitHub <noreply@github.com> "
                                   "1649269293 +0000\n\nNew test file"
                    }
                }
            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/git#create-a-commit"
                }
            )
        return self.response

    def patch_git_ref(self):
        if self.for_status is Status.SUCCESS:
            self.response.status = self.success['msg']
            self.response.status_code = self.success['status']
            self.response.data = dumps(
                {
                    "ref": "refs/heads/test_branch",
                    "node_id": "REF_kwDOG0SbL7ZyZWZzL2hlYWRzL3Rlc3RfYnJhbmNo",
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/refs/heads/test_branch",
                    "object": {
                        "sha": "7f0624ce1d9407aecae6e38dd007dea0265b12c2",
                        "type": "commit",
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/7f0624ce1d9407aecae6e38dd007dea0265b12c2"
                    }
                }

            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.status()
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/git#update-a-reference"
                }
            )
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
            self.response.status_code = self.success['status']
            self.response.status = self.success['msg']
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
            self.response.status_code = self.success['status']
            self.response.status = self.success['msg']
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

    def get_commit(self, blog_file: bool = False, blog_page_file: bool = False):
        if self.for_status is Status.SUCCESS and blog_file is False and blog_page_file is False:
            self.response.data = dumps(
                {
                    "sha": "10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "node_id": "C_kwDOG0SbL9oAKDEwZjY4NjgyODUwZDU5OGE5MGVkNmY1ZWEyMzdmNWIxNDBhNWY0ZjM",
                    "commit": {
                        "author": {
                            "name": "Adithya Shetty",
                            "email": "32545664+Maverick099@users.noreply.github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "committer": {
                            "name": "GitHub",
                            "email": "noreply@github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "message": "Create sunflower.dart",
                        "tree": {
                            "sha": "01136d7e2c770bd3fed8006c0d79fd694c7a9065",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/01136d7e2c770bd3fed8006c0d79fd694c7a9065"
                        },
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                        "comment_count": 0,
                        "verification": {
                            "verified": True,
                            "reason": "valid",
                            "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiCNUjCRBK7hj4Ov3rIwAAh6kIAGysqYujn3oEvP9g1DzkP5gg\nyfZiQemnGqhNgrn/roq3J7+dLp0wcf0YBWuWP1ivg7FOrPrzNSFrOj2yPLHgsUSa\n29gTpYUmwMfaEXBwNUdi82p8f80DkVWWzHrbUCziaGa2VxMzfntf1YQgB1W9SXHR\n6WZlDmf4g5R7Ik"
                                         "/Wm1rU3t3cLjEtGevSuum/UMPvR7ZRxxjIs7Cd4wzPCPJhSIr6\nl9nTnrWXGWTzK5mRae62Xz/QGYRw6hudNFU7oJxCPZjL+X8ZEkYUM/I9b8+Z0qIg\nE011PNJyKGiamOP6OH8lvKEZmnHAuM2F9zlrEyI6K1mWD0ycCr8K/7luUaBmt9Q=\n=stsj\n-----END PGP SIGNATURE-----\n",
                            "payload": "tree 01136d7e2c770bd3fed8006c0d79fd694c7a9065\nparent 9a4cb2a834ef6fb04e37b370eee075411c26c304\nauthor Adithya Shetty <32545664+Maverick099@users.noreply.github.com> 1644746019 +0530\ncommitter GitHub <noreply@github.com> 1644746019 +0530\n\nCreate "
                                       "sunflower.dart "
                        }
                    },
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "comments_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3/comments",
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
                    "committer": {
                        "login": "web-flow",
                        "id": 19864447,
                        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/web-flow",
                        "html_url": "https://github.com/web-flow",
                        "followers_url": "https://api.github.com/users/web-flow/followers",
                        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                        "organizations_url": "https://api.github.com/users/web-flow/orgs",
                        "repos_url": "https://api.github.com/users/web-flow/repos",
                        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/web-flow/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "parents": [
                        {
                            "sha": "9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/9a4cb2a834ef6fb04e37b370eee075411c26c304"
                        }
                    ],
                    "stats": {
                        "total": 147,
                        "additions": 147,
                        "deletions": 0
                    },
                    "files": [
                        {
                            "sha": "7616871141cc1b313bfd92271df48e505d29eb31",
                            "filename": "custom_card_design/lib/sunflower.dart",
                            "status": "added",
                            "additions": 147,
                            "deletions": 0,
                            "changes": 147,
                            "blob_url": "https://github.com/Coders-Asylum/fuzzy-train/blob/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "raw_url": "https://github.com/Coders-Asylum/fuzzy-train/raw/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "contents_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contents/custom_card_design%2Flib%2Fsunflower.dart?ref=10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                            "patch": "@@ -0,0 +1,147 @@\n+// Copyright 2019 the Dart project authors. All rights reserved.\n+// Use of this source code is governed by a BSD-style license\n+// that can be found in the LICENSE file.\n+\n+import 'dart:math' as math;\n+import "
                                     "'package:flutter/material.dart';\n+\n+const Color primaryColor = Colors.orange;\n+const TargetPlatform platform = TargetPlatform.android;\n+\n+void main() {\n+  runApp(Sunflower());\n+}\n+\n+class SunflowerPainter extends CustomPainter {\n+  static const "
                                     "seedRadius = 2.0;\n+  static const scaleFactor = 4;\n+  static const tau = math.pi * 2;\n+\n+  static final phi = (math.sqrt(5) + 1) / 2;\n+\n+  final int seeds;\n+\n+  SunflowerPainter(this.seeds);\n+\n+  @override\n+  void paint(Canvas canvas, "
                                     "Size size) {\n+    final center = size.width / 2;\n+\n+    for (var i = 0; i < seeds; i++) {\n+      final theta = i * tau / phi;\n+      final r = math.sqrt(i) * scaleFactor;\n+      final x = center + r * math.cos(theta);\n+      final y = center - r * "
                                     "math.sin(theta);\n+      final offset = Offset(x, y);\n+      if (!size.contains(offset)) {\n+        continue;\n+      }\n+      drawSeed(canvas, x, y);\n+    }\n+  }\n+\n+  @override\n+  bool shouldRepaint(SunflowerPainter oldDelegate) {\n+    return "
                                     "oldDelegate.seeds != seeds;\n+  }\n+\n+  // Draw a small circle representing a seed centered at (x,y).\n+  void drawSeed(Canvas canvas, double x, double y) {\n+    final paint = Paint()\n+      ..strokeWidth = 2\n+      ..style = PaintingStyle.fill\n+      "
                                     "..color = primaryColor;\n+    canvas.drawCircle(Offset(x, y), seedRadius, paint);\n+  }\n+}\n+\n+class Sunflower extends StatefulWidget {\n+  @override\n+  State<StatefulWidget> createState() {\n+    return _SunflowerState();\n+  }\n+}\n+\n+class "
                                     "_SunflowerState extends State<Sunflower> {\n+  double seeds = 100.0;\n+\n+  int get seedCount => seeds.floor();\n+\n+  @override\n+  Widget build(BuildContext context) {\n+    return MaterialApp(\n+      debugShowCheckedModeBanner: false,"
                                     "\n+      theme: ThemeData().copyWith(\n+        platform: platform,\n+        brightness: Brightness.dark,\n+        sliderTheme: SliderThemeData.fromPrimaryColors(\n+          primaryColor: primaryColor,\n+          primaryColorLight: primaryColor,"
                                     "\n+          primaryColorDark: primaryColor,\n+          valueIndicatorTextStyle: const DefaultTextStyle.fallback().style,\n+        ),\n+      ),\n+      home: Scaffold(\n+        appBar: AppBar(\n+          title: const Text(\"Sunflower\"),\n+        ),"
                                     "\n+        drawer: Drawer(\n+          child: ListView(\n+            children: const [\n+              DrawerHeader(\n+                child: Center(\n+                  child: Text(\n+                    \"Sunflower 🌻\",\n+                    style: "
                                     "TextStyle(fontSize: 32),\n+                  ),\n+                ),\n+              ),\n+            ],\n+          ),\n+        ),\n+        body: Container(\n+          constraints: const BoxConstraints.expand(),\n+          decoration: BoxDecoration(\n+   "
                                     "         border: Border.all(\n+              color: Colors.transparent,\n+            ),\n+          ),\n+          child: Column(\n+            crossAxisAlignment: CrossAxisAlignment.center,\n+            mainAxisAlignment: MainAxisAlignment.start,"
                                     "\n+            children: [\n+              Container(\n+                decoration: BoxDecoration(\n+                  border: Border.all(\n+                    color: Colors.transparent,\n+                  ),\n+                ),"
                                     "\n+                child: SizedBox(\n+                  width: 400,\n+                  height: 400,\n+                  child: CustomPaint(\n+                    painter: SunflowerPainter(seedCount),\n+                  ),\n+                ),"
                                     "\n+              ),\n+              Text(\"Showing $seedCount seeds\"),\n+              ConstrainedBox(\n+                constraints: const BoxConstraints.tightFor(width: 300),\n+                child: Slider.adaptive(\n+                  min: 20,"
                                     "\n+                  max: 2000,\n+                  value: seeds,\n+                  onChanged: (newValue) {\n+                    setState(() {\n+                      seeds = newValue;\n+                    });\n+                  },\n+                ),"
                                     "\n+              ),\n+            ],\n+          ),\n+        ),\n+      ),\n+    );\n+  }\n+} "
                        }
                    ]
                }
            )
        elif self.for_status is Status.SUCCESS and blog_file is True and blog_page_file is True:
            self.response.data = dumps(
                {
                    "sha": "10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "node_id": "C_kwDOG0SbL9oAKDEwZjY4NjgyODUwZDU5OGE5MGVkNmY1ZWEyMzdmNWIxNDBhNWY0ZjM",
                    "commit": {
                        "author": {
                            "name": "Adithya Shetty",
                            "email": "32545664+Maverick099@users.noreply.github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "committer": {
                            "name": "GitHub",
                            "email": "noreply@github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "message": "Create sunflower.dart",
                        "tree": {
                            "sha": "01136d7e2c770bd3fed8006c0d79fd694c7a9065",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/01136d7e2c770bd3fed8006c0d79fd694c7a9065"
                        },
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                        "comment_count": 0,
                        "verification": {
                            "verified": True,
                            "reason": "valid",
                            "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiCNUjCRBK7hj4Ov3rIwAAh6kIAGysqYujn3oEvP9g1DzkP5gg\nyfZiQemnGqhNgrn/roq3J7+dLp0wcf0YBWuWP1ivg7FOrPrzNSFrOj2yPLHgsUSa\n29gTpYUmwMfaEXBwNUdi82p8f80DkVWWzHrbUCziaGa2VxMzfntf1YQgB1W9SXHR\n6WZlDmf4g5R7Ik"
                                         "/Wm1rU3t3cLjEtGevSuum/UMPvR7ZRxxjIs7Cd4wzPCPJhSIr6\nl9nTnrWXGWTzK5mRae62Xz/QGYRw6hudNFU7oJxCPZjL+X8ZEkYUM/I9b8+Z0qIg\nE011PNJyKGiamOP6OH8lvKEZmnHAuM2F9zlrEyI6K1mWD0ycCr8K/7luUaBmt9Q=\n=stsj\n-----END PGP SIGNATURE-----\n",
                            "payload": "tree 01136d7e2c770bd3fed8006c0d79fd694c7a9065\nparent 9a4cb2a834ef6fb04e37b370eee075411c26c304\nauthor Adithya Shetty <32545664+Maverick099@users.noreply.github.com> 1644746019 +0530\ncommitter GitHub <noreply@github.com> 1644746019 +0530\n\nCreate "
                                       "sunflower.dart "
                        }
                    },
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "comments_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3/comments",
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
                    "committer": {
                        "login": "web-flow",
                        "id": 19864447,
                        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/web-flow",
                        "html_url": "https://github.com/web-flow",
                        "followers_url": "https://api.github.com/users/web-flow/followers",
                        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                        "organizations_url": "https://api.github.com/users/web-flow/orgs",
                        "repos_url": "https://api.github.com/users/web-flow/repos",
                        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/web-flow/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "parents": [
                        {
                            "sha": "9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/9a4cb2a834ef6fb04e37b370eee075411c26c304"
                        }
                    ],
                    "stats": {
                        "total": 147,
                        "additions": 147,
                        "deletions": 0
                    },
                    "files": [
                        {
                            "sha": "7616871141cc1b313bfd92271df48e505d29eb31",
                            "filename": "lib/pages/BlogPage.dart",
                            "status": "added",
                            "additions": 147,
                            "deletions": 0,
                            "changes": 147,
                            "blob_url": "https://github.com/Coders-Asylum/fuzzy-train/blob/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "raw_url": "https://github.com/Coders-Asylum/fuzzy-train/raw/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "contents_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contents/custom_card_design%2Flib%2Fsunflower.dart?ref=10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                            "patch": "@@ -0,0 +1,147 @@\n+// Copyright 2019 the Dart project authors. All rights reserved.\n+// Use of this source code is governed by a BSD-style license\n+// that can be found in the LICENSE file.\n+\n+import 'dart:math' as math;\n+import "
                                     "'package:flutter/material.dart';\n+\n+const Color primaryColor = Colors.orange;\n+const TargetPlatform platform = TargetPlatform.android;\n+\n+void main() {\n+  runApp(Sunflower());\n+}\n+\n+class SunflowerPainter extends CustomPainter {\n+  static const "
                                     "seedRadius = 2.0;\n+  static const scaleFactor = 4;\n+  static const tau = math.pi * 2;\n+\n+  static final phi = (math.sqrt(5) + 1) / 2;\n+\n+  final int seeds;\n+\n+  SunflowerPainter(this.seeds);\n+\n+  @override\n+  void paint(Canvas canvas, "
                                     "Size size) {\n+    final center = size.width / 2;\n+\n+    for (var i = 0; i < seeds; i++) {\n+      final theta = i * tau / phi;\n+      final r = math.sqrt(i) * scaleFactor;\n+      final x = center + r * math.cos(theta);\n+      final y = center - r * "
                                     "math.sin(theta);\n+      final offset = Offset(x, y);\n+      if (!size.contains(offset)) {\n+        continue;\n+      }\n+      drawSeed(canvas, x, y);\n+    }\n+  }\n+\n+  @override\n+  bool shouldRepaint(SunflowerPainter oldDelegate) {\n+    return "
                                     "oldDelegate.seeds != seeds;\n+  }\n+\n+  // Draw a small circle representing a seed centered at (x,y).\n+  void drawSeed(Canvas canvas, double x, double y) {\n+    final paint = Paint()\n+      ..strokeWidth = 2\n+      ..style = PaintingStyle.fill\n+      "
                                     "..color = primaryColor;\n+    canvas.drawCircle(Offset(x, y), seedRadius, paint);\n+  }\n+}\n+\n+class Sunflower extends StatefulWidget {\n+  @override\n+  State<StatefulWidget> createState() {\n+    return _SunflowerState();\n+  }\n+}\n+\n+class "
                                     "_SunflowerState extends State<Sunflower> {\n+  double seeds = 100.0;\n+\n+  int get seedCount => seeds.floor();\n+\n+  @override\n+  Widget build(BuildContext context) {\n+    return MaterialApp(\n+      debugShowCheckedModeBanner: false,"
                                     "\n+      theme: ThemeData().copyWith(\n+        platform: platform,\n+        brightness: Brightness.dark,\n+        sliderTheme: SliderThemeData.fromPrimaryColors(\n+          primaryColor: primaryColor,\n+          primaryColorLight: primaryColor,"
                                     "\n+          primaryColorDark: primaryColor,\n+          valueIndicatorTextStyle: const DefaultTextStyle.fallback().style,\n+        ),\n+      ),\n+      home: Scaffold(\n+        appBar: AppBar(\n+          title: const Text(\"Sunflower\"),\n+        ),"
                                     "\n+        drawer: Drawer(\n+          child: ListView(\n+            children: const [\n+              DrawerHeader(\n+                child: Center(\n+                  child: Text(\n+                    \"Sunflower 🌻\",\n+                    style: "
                                     "TextStyle(fontSize: 32),\n+                  ),\n+                ),\n+              ),\n+            ],\n+          ),\n+        ),\n+        body: Container(\n+          constraints: const BoxConstraints.expand(),\n+          decoration: BoxDecoration(\n+   "
                                     "         border: Border.all(\n+              color: Colors.transparent,\n+            ),\n+          ),\n+          child: Column(\n+            crossAxisAlignment: CrossAxisAlignment.center,\n+            mainAxisAlignment: MainAxisAlignment.start,"
                                     "\n+            children: [\n+              Container(\n+                decoration: BoxDecoration(\n+                  border: Border.all(\n+                    color: Colors.transparent,\n+                  ),\n+                ),"
                                     "\n+                child: SizedBox(\n+                  width: 400,\n+                  height: 400,\n+                  child: CustomPaint(\n+                    painter: SunflowerPainter(seedCount),\n+                  ),\n+                ),"
                                     "\n+              ),\n+              Text(\"Showing $seedCount seeds\"),\n+              ConstrainedBox(\n+                constraints: const BoxConstraints.tightFor(width: 300),\n+                child: Slider.adaptive(\n+                  min: 20,"
                                     "\n+                  max: 2000,\n+                  value: seeds,\n+                  onChanged: (newValue) {\n+                    setState(() {\n+                      seeds = newValue;\n+                    });\n+                  },\n+                ),"
                                     "\n+              ),\n+            ],\n+          ),\n+        ),\n+      ),\n+    );\n+  }\n+} "
                        },
                        {
                            "sha": "7616871141cc1b31das3d92271df48e505d29eb31",
                            "filename": "lib/pages/BlogPostPage.dart",
                            "status": "added",
                            "additions": 147,
                            "deletions": 0,
                            "changes": 147,
                            "blob_url": "https://github.com/Coders-Asylum/fuzzy-train/blob/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "raw_url": "https://github.com/Coders-Asylum/fuzzy-train/raw/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "contents_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contents/custom_card_design%2Flib%2Fsunflower.dart?ref=10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                            "patch": "@@ -0,0 +1,147 @@\n+// Copyright 2019 the Dart project authors. All rights reserved.\n+// Use of this source code is governed by a BSD-style license\n+// that can be found in the LICENSE file.\n+\n+import 'dart:math' as math;\n+import "
                                     "'package:flutter/material.dart';\n+\n+const Color primaryColor = Colors.orange;\n+const TargetPlatform platform = TargetPlatform.android;\n+\n+void main() {\n+  runApp(Sunflower());\n+}\n+\n+class SunflowerPainter extends CustomPainter {\n+  static const "
                                     "seedRadius = 2.0;\n+  static const scaleFactor = 4;\n+  static const tau = math.pi * 2;\n+\n+  static final phi = (math.sqrt(5) + 1) / 2;\n+\n+  final int seeds;\n+\n+  SunflowerPainter(this.seeds);\n+\n+  @override\n+  void paint(Canvas canvas, "
                                     "Size size) {\n+    final center = size.width / 2;\n+\n+    for (var i = 0; i < seeds; i++) {\n+      final theta = i * tau / phi;\n+      final r = math.sqrt(i) * scaleFactor;\n+      final x = center + r * math.cos(theta);\n+      final y = center - r * "
                                     "math.sin(theta);\n+      final offset = Offset(x, y);\n+      if (!size.contains(offset)) {\n+        continue;\n+      }\n+      drawSeed(canvas, x, y);\n+    }\n+  }\n+\n+  @override\n+  bool shouldRepaint(SunflowerPainter oldDelegate) {\n+    return "
                                     "oldDelegate.seeds != seeds;\n+  }\n+\n+  // Draw a small circle representing a seed centered at (x,y).\n+  void drawSeed(Canvas canvas, double x, double y) {\n+    final paint = Paint()\n+      ..strokeWidth = 2\n+      ..style = PaintingStyle.fill\n+      "
                                     "..color = primaryColor;\n+    canvas.drawCircle(Offset(x, y), seedRadius, paint);\n+  }\n+}\n+\n+class Sunflower extends StatefulWidget {\n+  @override\n+  State<StatefulWidget> createState() {\n+    return _SunflowerState();\n+  }\n+}\n+\n+class "
                                     "_SunflowerState extends State<Sunflower> {\n+  double seeds = 100.0;\n+\n+  int get seedCount => seeds.floor();\n+\n+  @override\n+  Widget build(BuildContext context) {\n+    return MaterialApp(\n+      debugShowCheckedModeBanner: false,"
                                     "\n+      theme: ThemeData().copyWith(\n+        platform: platform,\n+        brightness: Brightness.dark,\n+        sliderTheme: SliderThemeData.fromPrimaryColors(\n+          primaryColor: primaryColor,\n+          primaryColorLight: primaryColor,"
                                     "\n+          primaryColorDark: primaryColor,\n+          valueIndicatorTextStyle: const DefaultTextStyle.fallback().style,\n+        ),\n+      ),\n+      home: Scaffold(\n+        appBar: AppBar(\n+          title: const Text(\"Sunflower\"),\n+        ),"
                                     "\n+        drawer: Drawer(\n+          child: ListView(\n+            children: const [\n+              DrawerHeader(\n+                child: Center(\n+                  child: Text(\n+                    \"Sunflower 🌻\",\n+                    style: "
                                     "TextStyle(fontSize: 32),\n+                  ),\n+                ),\n+              ),\n+            ],\n+          ),\n+        ),\n+        body: Container(\n+          constraints: const BoxConstraints.expand(),\n+          decoration: BoxDecoration(\n+   "
                                     "         border: Border.all(\n+              color: Colors.transparent,\n+            ),\n+          ),\n+          child: Column(\n+            crossAxisAlignment: CrossAxisAlignment.center,\n+            mainAxisAlignment: MainAxisAlignment.start,"
                                     "\n+            children: [\n+              Container(\n+                decoration: BoxDecoration(\n+                  border: Border.all(\n+                    color: Colors.transparent,\n+                  ),\n+                ),"
                                     "\n+                child: SizedBox(\n+                  width: 400,\n+                  height: 400,\n+                  child: CustomPaint(\n+                    painter: SunflowerPainter(seedCount),\n+                  ),\n+                ),"
                                     "\n+              ),\n+              Text(\"Showing $seedCount seeds\"),\n+              ConstrainedBox(\n+                constraints: const BoxConstraints.tightFor(width: 300),\n+                child: Slider.adaptive(\n+                  min: 20,"
                                     "\n+                  max: 2000,\n+                  value: seeds,\n+                  onChanged: (newValue) {\n+                    setState(() {\n+                      seeds = newValue;\n+                    });\n+                  },\n+                ),"
                                     "\n+              ),\n+            ],\n+          ),\n+        ),\n+      ),\n+    );\n+  }\n+} "
                        }
                    ]
                }
            )
        elif self.for_status is Status.SUCCESS and blog_file is False and blog_page_file is True:
            self.response.data = dumps(
                {
                    "sha": "10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "node_id": "C_kwDOG0SbL9oAKDEwZjY4NjgyODUwZDU5OGE5MGVkNmY1ZWEyMzdmNWIxNDBhNWY0ZjM",
                    "commit": {
                        "author": {
                            "name": "Adithya Shetty",
                            "email": "32545664+Maverick099@users.noreply.github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "committer": {
                            "name": "GitHub",
                            "email": "noreply@github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "message": "Create sunflower.dart",
                        "tree": {
                            "sha": "01136d7e2c770bd3fed8006c0d79fd694c7a9065",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/01136d7e2c770bd3fed8006c0d79fd694c7a9065"
                        },
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                        "comment_count": 0,
                        "verification": {
                            "verified": True,
                            "reason": "valid",
                            "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiCNUjCRBK7hj4Ov3rIwAAh6kIAGysqYujn3oEvP9g1DzkP5gg\nyfZiQemnGqhNgrn/roq3J7+dLp0wcf0YBWuWP1ivg7FOrPrzNSFrOj2yPLHgsUSa\n29gTpYUmwMfaEXBwNUdi82p8f80DkVWWzHrbUCziaGa2VxMzfntf1YQgB1W9SXHR\n6WZlDmf4g5R7Ik"
                                         "/Wm1rU3t3cLjEtGevSuum/UMPvR7ZRxxjIs7Cd4wzPCPJhSIr6\nl9nTnrWXGWTzK5mRae62Xz/QGYRw6hudNFU7oJxCPZjL+X8ZEkYUM/I9b8+Z0qIg\nE011PNJyKGiamOP6OH8lvKEZmnHAuM2F9zlrEyI6K1mWD0ycCr8K/7luUaBmt9Q=\n=stsj\n-----END PGP SIGNATURE-----\n",
                            "payload": "tree 01136d7e2c770bd3fed8006c0d79fd694c7a9065\nparent 9a4cb2a834ef6fb04e37b370eee075411c26c304\nauthor Adithya Shetty <32545664+Maverick099@users.noreply.github.com> 1644746019 +0530\ncommitter GitHub <noreply@github.com> 1644746019 +0530\n\nCreate "
                                       "sunflower.dart "
                        }
                    },
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "comments_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3/comments",
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
                    "committer": {
                        "login": "web-flow",
                        "id": 19864447,
                        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/web-flow",
                        "html_url": "https://github.com/web-flow",
                        "followers_url": "https://api.github.com/users/web-flow/followers",
                        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                        "organizations_url": "https://api.github.com/users/web-flow/orgs",
                        "repos_url": "https://api.github.com/users/web-flow/repos",
                        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/web-flow/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "parents": [
                        {
                            "sha": "9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/9a4cb2a834ef6fb04e37b370eee075411c26c304"
                        }
                    ],
                    "stats": {
                        "total": 147,
                        "additions": 147,
                        "deletions": 0
                    },
                    "files": [
                        {
                            "sha": "7616871141cc1b31das3d92271df48e505d29eb31",
                            "filename": "lib/pages/BlogPostPage.dart",
                            "status": "added",
                            "additions": 147,
                            "deletions": 0,
                            "changes": 147,
                            "blob_url": "https://github.com/Coders-Asylum/fuzzy-train/blob/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "raw_url": "https://github.com/Coders-Asylum/fuzzy-train/raw/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "contents_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contents/custom_card_design%2Flib%2Fsunflower.dart?ref=10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                            "patch": "@@ -0,0 +1,147 @@\n+// Copyright 2019 the Dart project authors. All rights reserved.\n+// Use of this source code is governed by a BSD-style license\n+// that can be found in the LICENSE file.\n+\n+import 'dart:math' as math;\n+import "
                                     "'package:flutter/material.dart';\n+\n+const Color primaryColor = Colors.orange;\n+const TargetPlatform platform = TargetPlatform.android;\n+\n+void main() {\n+  runApp(Sunflower());\n+}\n+\n+class SunflowerPainter extends CustomPainter {\n+  static const "
                                     "seedRadius = 2.0;\n+  static const scaleFactor = 4;\n+  static const tau = math.pi * 2;\n+\n+  static final phi = (math.sqrt(5) + 1) / 2;\n+\n+  final int seeds;\n+\n+  SunflowerPainter(this.seeds);\n+\n+  @override\n+  void paint(Canvas canvas, "
                                     "Size size) {\n+    final center = size.width / 2;\n+\n+    for (var i = 0; i < seeds; i++) {\n+      final theta = i * tau / phi;\n+      final r = math.sqrt(i) * scaleFactor;\n+      final x = center + r * math.cos(theta);\n+      final y = center - r * "
                                     "math.sin(theta);\n+      final offset = Offset(x, y);\n+      if (!size.contains(offset)) {\n+        continue;\n+      }\n+      drawSeed(canvas, x, y);\n+    }\n+  }\n+\n+  @override\n+  bool shouldRepaint(SunflowerPainter oldDelegate) {\n+    return "
                                     "oldDelegate.seeds != seeds;\n+  }\n+\n+  // Draw a small circle representing a seed centered at (x,y).\n+  void drawSeed(Canvas canvas, double x, double y) {\n+    final paint = Paint()\n+      ..strokeWidth = 2\n+      ..style = PaintingStyle.fill\n+      "
                                     "..color = primaryColor;\n+    canvas.drawCircle(Offset(x, y), seedRadius, paint);\n+  }\n+}\n+\n+class Sunflower extends StatefulWidget {\n+  @override\n+  State<StatefulWidget> createState() {\n+    return _SunflowerState();\n+  }\n+}\n+\n+class "
                                     "_SunflowerState extends State<Sunflower> {\n+  double seeds = 100.0;\n+\n+  int get seedCount => seeds.floor();\n+\n+  @override\n+  Widget build(BuildContext context) {\n+    return MaterialApp(\n+      debugShowCheckedModeBanner: false,"
                                     "\n+      theme: ThemeData().copyWith(\n+        platform: platform,\n+        brightness: Brightness.dark,\n+        sliderTheme: SliderThemeData.fromPrimaryColors(\n+          primaryColor: primaryColor,\n+          primaryColorLight: primaryColor,"
                                     "\n+          primaryColorDark: primaryColor,\n+          valueIndicatorTextStyle: const DefaultTextStyle.fallback().style,\n+        ),\n+      ),\n+      home: Scaffold(\n+        appBar: AppBar(\n+          title: const Text(\"Sunflower\"),\n+        ),"
                                     "\n+        drawer: Drawer(\n+          child: ListView(\n+            children: const [\n+              DrawerHeader(\n+                child: Center(\n+                  child: Text(\n+                    \"Sunflower 🌻\",\n+                    style: "
                                     "TextStyle(fontSize: 32),\n+                  ),\n+                ),\n+              ),\n+            ],\n+          ),\n+        ),\n+        body: Container(\n+          constraints: const BoxConstraints.expand(),\n+          decoration: BoxDecoration(\n+   "
                                     "         border: Border.all(\n+              color: Colors.transparent,\n+            ),\n+          ),\n+          child: Column(\n+            crossAxisAlignment: CrossAxisAlignment.center,\n+            mainAxisAlignment: MainAxisAlignment.start,"
                                     "\n+            children: [\n+              Container(\n+                decoration: BoxDecoration(\n+                  border: Border.all(\n+                    color: Colors.transparent,\n+                  ),\n+                ),"
                                     "\n+                child: SizedBox(\n+                  width: 400,\n+                  height: 400,\n+                  child: CustomPaint(\n+                    painter: SunflowerPainter(seedCount),\n+                  ),\n+                ),"
                                     "\n+              ),\n+              Text(\"Showing $seedCount seeds\"),\n+              ConstrainedBox(\n+                constraints: const BoxConstraints.tightFor(width: 300),\n+                child: Slider.adaptive(\n+                  min: 20,"
                                     "\n+                  max: 2000,\n+                  value: seeds,\n+                  onChanged: (newValue) {\n+                    setState(() {\n+                      seeds = newValue;\n+                    });\n+                  },\n+                ),"
                                     "\n+              ),\n+            ],\n+          ),\n+        ),\n+      ),\n+    );\n+  }\n+} "
                        }
                    ]
                }
            )
        elif self.for_status is Status.SUCCESS and blog_file is True and blog_page_file is False:
            self.response.data = dumps(
                {
                    "sha": "10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "node_id": "C_kwDOG0SbL9oAKDEwZjY4NjgyODUwZDU5OGE5MGVkNmY1ZWEyMzdmNWIxNDBhNWY0ZjM",
                    "commit": {
                        "author": {
                            "name": "Adithya Shetty",
                            "email": "32545664+Maverick099@users.noreply.github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "committer": {
                            "name": "GitHub",
                            "email": "noreply@github.com",
                            "date": "2022-02-13T09:53:39Z"
                        },
                        "message": "Create sunflower.dart",
                        "tree": {
                            "sha": "01136d7e2c770bd3fed8006c0d79fd694c7a9065",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/trees/01136d7e2c770bd3fed8006c0d79fd694c7a9065"
                        },
                        "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/git/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                        "comment_count": 0,
                        "verification": {
                            "verified": True,
                            "reason": "valid",
                            "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiCNUjCRBK7hj4Ov3rIwAAh6kIAGysqYujn3oEvP9g1DzkP5gg\nyfZiQemnGqhNgrn/roq3J7+dLp0wcf0YBWuWP1ivg7FOrPrzNSFrOj2yPLHgsUSa\n29gTpYUmwMfaEXBwNUdi82p8f80DkVWWzHrbUCziaGa2VxMzfntf1YQgB1W9SXHR\n6WZlDmf4g5R7Ik"
                                         "/Wm1rU3t3cLjEtGevSuum/UMPvR7ZRxxjIs7Cd4wzPCPJhSIr6\nl9nTnrWXGWTzK5mRae62Xz/QGYRw6hudNFU7oJxCPZjL+X8ZEkYUM/I9b8+Z0qIg\nE011PNJyKGiamOP6OH8lvKEZmnHAuM2F9zlrEyI6K1mWD0ycCr8K/7luUaBmt9Q=\n=stsj\n-----END PGP SIGNATURE-----\n",
                            "payload": "tree 01136d7e2c770bd3fed8006c0d79fd694c7a9065\nparent 9a4cb2a834ef6fb04e37b370eee075411c26c304\nauthor Adithya Shetty <32545664+Maverick099@users.noreply.github.com> 1644746019 +0530\ncommitter GitHub <noreply@github.com> 1644746019 +0530\n\nCreate "
                                       "sunflower.dart "
                        }
                    },
                    "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                    "comments_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/10f68682850d598a90ed6f5ea237f5b140a5f4f3/comments",
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
                    "committer": {
                        "login": "web-flow",
                        "id": 19864447,
                        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
                        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/web-flow",
                        "html_url": "https://github.com/web-flow",
                        "followers_url": "https://api.github.com/users/web-flow/followers",
                        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
                        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
                        "organizations_url": "https://api.github.com/users/web-flow/orgs",
                        "repos_url": "https://api.github.com/users/web-flow/repos",
                        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/web-flow/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "parents": [
                        {
                            "sha": "9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/commits/9a4cb2a834ef6fb04e37b370eee075411c26c304",
                            "html_url": "https://github.com/Coders-Asylum/fuzzy-train/commit/9a4cb2a834ef6fb04e37b370eee075411c26c304"
                        }
                    ],
                    "stats": {
                        "total": 147,
                        "additions": 147,
                        "deletions": 0
                    },
                    "files": [
                        {
                            "sha": "7616871141cc1b313bfd92271df48e505d29eb31",
                            "filename": "lib/pages/BlogPage.dart",
                            "status": "added",
                            "additions": 147,
                            "deletions": 0,
                            "changes": 147,
                            "blob_url": "https://github.com/Coders-Asylum/fuzzy-train/blob/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "raw_url": "https://github.com/Coders-Asylum/fuzzy-train/raw/10f68682850d598a90ed6f5ea237f5b140a5f4f3/custom_card_design%2Flib%2Fsunflower.dart",
                            "contents_url": "https://api.github.com/repos/Coders-Asylum/fuzzy-train/contents/custom_card_design%2Flib%2Fsunflower.dart?ref=10f68682850d598a90ed6f5ea237f5b140a5f4f3",
                            "patch": "@@ -0,0 +1,147 @@\n+// Copyright 2019 the Dart project authors. All rights reserved.\n+// Use of this source code is governed by a BSD-style license\n+// that can be found in the LICENSE file.\n+\n+import 'dart:math' as math;\n+import "
                                     "'package:flutter/material.dart';\n+\n+const Color primaryColor = Colors.orange;\n+const TargetPlatform platform = TargetPlatform.android;\n+\n+void main() {\n+  runApp(Sunflower());\n+}\n+\n+class SunflowerPainter extends CustomPainter {\n+  static const "
                                     "seedRadius = 2.0;\n+  static const scaleFactor = 4;\n+  static const tau = math.pi * 2;\n+\n+  static final phi = (math.sqrt(5) + 1) / 2;\n+\n+  final int seeds;\n+\n+  SunflowerPainter(this.seeds);\n+\n+  @override\n+  void paint(Canvas canvas, "
                                     "Size size) {\n+    final center = size.width / 2;\n+\n+    for (var i = 0; i < seeds; i++) {\n+      final theta = i * tau / phi;\n+      final r = math.sqrt(i) * scaleFactor;\n+      final x = center + r * math.cos(theta);\n+      final y = center - r * "
                                     "math.sin(theta);\n+      final offset = Offset(x, y);\n+      if (!size.contains(offset)) {\n+        continue;\n+      }\n+      drawSeed(canvas, x, y);\n+    }\n+  }\n+\n+  @override\n+  bool shouldRepaint(SunflowerPainter oldDelegate) {\n+    return "
                                     "oldDelegate.seeds != seeds;\n+  }\n+\n+  // Draw a small circle representing a seed centered at (x,y).\n+  void drawSeed(Canvas canvas, double x, double y) {\n+    final paint = Paint()\n+      ..strokeWidth = 2\n+      ..style = PaintingStyle.fill\n+      "
                                     "..color = primaryColor;\n+    canvas.drawCircle(Offset(x, y), seedRadius, paint);\n+  }\n+}\n+\n+class Sunflower extends StatefulWidget {\n+  @override\n+  State<StatefulWidget> createState() {\n+    return _SunflowerState();\n+  }\n+}\n+\n+class "
                                     "_SunflowerState extends State<Sunflower> {\n+  double seeds = 100.0;\n+\n+  int get seedCount => seeds.floor();\n+\n+  @override\n+  Widget build(BuildContext context) {\n+    return MaterialApp(\n+      debugShowCheckedModeBanner: false,"
                                     "\n+      theme: ThemeData().copyWith(\n+        platform: platform,\n+        brightness: Brightness.dark,\n+        sliderTheme: SliderThemeData.fromPrimaryColors(\n+          primaryColor: primaryColor,\n+          primaryColorLight: primaryColor,"
                                     "\n+          primaryColorDark: primaryColor,\n+          valueIndicatorTextStyle: const DefaultTextStyle.fallback().style,\n+        ),\n+      ),\n+      home: Scaffold(\n+        appBar: AppBar(\n+          title: const Text(\"Sunflower\"),\n+        ),"
                                     "\n+        drawer: Drawer(\n+          child: ListView(\n+            children: const [\n+              DrawerHeader(\n+                child: Center(\n+                  child: Text(\n+                    \"Sunflower 🌻\",\n+                    style: "
                                     "TextStyle(fontSize: 32),\n+                  ),\n+                ),\n+              ),\n+            ],\n+          ),\n+        ),\n+        body: Container(\n+          constraints: const BoxConstraints.expand(),\n+          decoration: BoxDecoration(\n+   "
                                     "         border: Border.all(\n+              color: Colors.transparent,\n+            ),\n+          ),\n+          child: Column(\n+            crossAxisAlignment: CrossAxisAlignment.center,\n+            mainAxisAlignment: MainAxisAlignment.start,"
                                     "\n+            children: [\n+              Container(\n+                decoration: BoxDecoration(\n+                  border: Border.all(\n+                    color: Colors.transparent,\n+                  ),\n+                ),"
                                     "\n+                child: SizedBox(\n+                  width: 400,\n+                  height: 400,\n+                  child: CustomPaint(\n+                    painter: SunflowerPainter(seedCount),\n+                  ),\n+                ),"
                                     "\n+              ),\n+              Text(\"Showing $seedCount seeds\"),\n+              ConstrainedBox(\n+                constraints: const BoxConstraints.tightFor(width: 300),\n+                child: Slider.adaptive(\n+                  min: 20,"
                                     "\n+                  max: 2000,\n+                  value: seeds,\n+                  onChanged: (newValue) {\n+                    setState(() {\n+                      seeds = newValue;\n+                    });\n+                  },\n+                ),"
                                     "\n+              ),\n+            ],\n+          ),\n+        ),\n+      ),\n+    );\n+  }\n+} "
                        }
                    ]
                }
            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "No commit found for SHA: {sha}",
                    "documentation_url": "https://docs.github.com/rest/reference/repos#get-a-commit"
                }
            )
        return self.response

    def get_raw_data(self):
        if self.for_status is Status.SUCCESS:
            self.response.data = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis at tellus at urna condimentum mattis pellentesque id. Lobortis elementum nibh tellus molestie nunc non. Vestibulum lectus mauris ' \
                                 'ultrices eros in. Odio ut sem nulla pharetra. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Nam libero justo laoreet sit amet cursus. Amet nulla facilisi morbi tempus iaculis urna. Massa id neque aliquam vestibulum morbi blandit cursus risus at. ' \
                                 'Mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Lobortis feugiat vivamus at augue eget arcu dictum. Sit amet consectetur adipiscing elit pellentesque. Tortor posuere ac ut consequat semper viverra nam libero justo. Eu nisl nunc mi ipsum faucibus ' \
                                 'vitae. Semper feugiat nibh sed pulvinar proin gravida hendrerit. Habitant morbi tristique senectus et netus et. Tempor orci dapibus ultrices in iaculis nunc. Amet risus nullam eget felis eget nunc lobortis mattis. Posuere sollicitudin aliquam ultrices sagittis ' \
                                 'orci. '
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = "Not found"

        return self.response

    def get_milestone(self):
        if self.for_status is Status.SUCCESS:
            self.response.data = dumps(
                [
                    {
                        "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
                        "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
                        "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
                        "id": 1002604,
                        "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
                        "number": 1,
                        "state": "open",
                        "title": "v1.0",
                        "description": "Tracking milestone for version 1.0",
                        "creator": {
                            "login": "octocat",
                            "id": 1,
                            "node_id": "MDQ6VXNlcjE=",
                            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/octocat",
                            "html_url": "https://github.com/octocat",
                            "followers_url": "https://api.github.com/users/octocat/followers",
                            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                            "organizations_url": "https://api.github.com/users/octocat/orgs",
                            "repos_url": "https://api.github.com/users/octocat/repos",
                            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/octocat/received_events",
                            "type": "User",
                            "site_admin": False
                        },
                        "open_issues": 4,
                        "closed_issues": 8,
                        "created_at": "2011-04-10T20:09:31Z",
                        "updated_at": "2014-03-03T18:58:10Z",
                        "closed_at": "2013-02-12T13:22:01Z",
                        "due_on": "2012-10-09T23:39:01Z"
                    }
                ]
            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/reference/issues#list-milestones"
                }
            )
        return self.response

    def create_issue(self):
        if self.for_status is Status.SUCCESS:
            self.response.status_code = self.created['status']
            self.response.status = self.created['msg']
            self.response.data = dumps(
                {
                    "id": 1,
                    "node_id": "MDU6SXNzdWUx",
                    "url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
                    "repository_url": "https://api.github.com/repos/octocat/Hello-World",
                    "labels_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/labels{/name}",
                    "comments_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/comments",
                    "events_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/events",
                    "html_url": "https://github.com/octocat/Hello-World/issues/1347",
                    "number": 1347,
                    "state": "open",
                    "title": "Found a bug",
                    "body": "I'm having a problem with this.",
                    "user": {
                        "login": "octocat",
                        "id": 1,
                        "node_id": "MDQ6VXNlcjE=",
                        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/octocat",
                        "html_url": "https://github.com/octocat",
                        "followers_url": "https://api.github.com/users/octocat/followers",
                        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                        "organizations_url": "https://api.github.com/users/octocat/orgs",
                        "repos_url": "https://api.github.com/users/octocat/repos",
                        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/octocat/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "labels": [
                        {
                            "id": 208045946,
                            "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
                            "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
                            "name": "bug",
                            "description": "Something isn't working",
                            "color": "f29513",
                            "default": True
                        }
                    ],
                    "assignee": {
                        "login": "octocat",
                        "id": 1,
                        "node_id": "MDQ6VXNlcjE=",
                        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/octocat",
                        "html_url": "https://github.com/octocat",
                        "followers_url": "https://api.github.com/users/octocat/followers",
                        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                        "organizations_url": "https://api.github.com/users/octocat/orgs",
                        "repos_url": "https://api.github.com/users/octocat/repos",
                        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/octocat/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "assignees": [
                        {
                            "login": "octocat",
                            "id": 1,
                            "node_id": "MDQ6VXNlcjE=",
                            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/octocat",
                            "html_url": "https://github.com/octocat",
                            "followers_url": "https://api.github.com/users/octocat/followers",
                            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                            "organizations_url": "https://api.github.com/users/octocat/orgs",
                            "repos_url": "https://api.github.com/users/octocat/repos",
                            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/octocat/received_events",
                            "type": "User",
                            "site_admin": False
                        }
                    ],
                    "milestone": {
                        "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1",
                        "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
                        "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
                        "id": 1002604,
                        "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
                        "number": 1,
                        "state": "open",
                        "title": "v1.0",
                        "description": "Tracking milestone for version 1.0",
                        "creator": {
                            "login": "octocat",
                            "id": 1,
                            "node_id": "MDQ6VXNlcjE=",
                            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                            "gravatar_id": "",
                            "url": "https://api.github.com/users/octocat",
                            "html_url": "https://github.com/octocat",
                            "followers_url": "https://api.github.com/users/octocat/followers",
                            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                            "organizations_url": "https://api.github.com/users/octocat/orgs",
                            "repos_url": "https://api.github.com/users/octocat/repos",
                            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                            "received_events_url": "https://api.github.com/users/octocat/received_events",
                            "type": "User",
                            "site_admin": False
                        },
                        "open_issues": 4,
                        "closed_issues": 8,
                        "created_at": "2011-04-10T20:09:31Z",
                        "updated_at": "2014-03-03T18:58:10Z",
                        "closed_at": "2013-02-12T13:22:01Z",
                        "due_on": "2012-10-09T23:39:01Z"
                    },
                    "locked": True,
                    "active_lock_reason": "too heated",
                    "comments": 0,
                    "pull_request": {
                        "url": "https://api.github.com/repos/octocat/Hello-World/pulls/1347",
                        "html_url": "https://github.com/octocat/Hello-World/pull/1347",
                        "diff_url": "https://github.com/octocat/Hello-World/pull/1347.diff",
                        "patch_url": "https://github.com/octocat/Hello-World/pull/1347.patch"
                    },
                    "closed_at": None,
                    "created_at": "2011-04-22T13:33:48Z",
                    "updated_at": "2011-04-22T13:33:48Z",
                    "closed_by": {
                        "login": "octocat",
                        "id": 1,
                        "node_id": "MDQ6VXNlcjE=",
                        "avatar_url": "https://github.com/images/error/octocat_happy.gif",
                        "gravatar_id": "",
                        "url": "https://api.github.com/users/octocat",
                        "html_url": "https://github.com/octocat",
                        "followers_url": "https://api.github.com/users/octocat/followers",
                        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
                        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
                        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
                        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
                        "organizations_url": "https://api.github.com/users/octocat/orgs",
                        "repos_url": "https://api.github.com/users/octocat/repos",
                        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
                        "received_events_url": "https://api.github.com/users/octocat/received_events",
                        "type": "User",
                        "site_admin": False
                    },
                    "author_association": "COLLABORATOR"
                }
            )
        elif self.for_status is Status.RES_NOT_FOUND:
            self.response.data = dumps(
                {
                    "message": "Not Found",
                    "documentation_url": "https://docs.github.com/en/rest/issues/issues#create-an-issue"
                }
            )
        return self.response
