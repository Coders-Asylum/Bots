from unittest import TestCase, main
from requests import get
from json import loads
from requests.structures import CaseInsensitiveDict
from os import environ
from bin.handlers import GithubAPIHandler, GithubRefObject, GithubAppApi
from datetime import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from jwt import encode


class TestGithubAPIHandler(TestCase):
    g = GithubAPIHandler()
    owner = 'Coders-Asylum'
    repo = 'fuzzy-train'
    branch = 'test_branch'

    header: CaseInsensitiveDict = CaseInsensitiveDict()
    header['Accept'] = 'application/vnd.github.v3+json'

    def test_download_repo_file(self):
        expected_file_contents: str = '// This is a basic Flutter widget test.\n//\n' \
                                      '// To perform an interaction with a widget in your test, use the WidgetTester\n' \
                                      '// utility that Flutter provides. For example, you can send tap and scroll\n' \
                                      '// gestures. You can also use WidgetTester to find child widgets in the widget\n' \
                                      '// tree, read text, and verify that the values of widget properties are ' \
                                      'correct.\n\n' \
                                      "import 'package:flutter/material.dart';\n" \
                                      "import 'package:flutter_test/flutter_test.dart';\n\n" \
                                      "import 'package:custom_card_design/main.dart';\n\n" \
                                      'void main() {\n' \
                                      '  testWidgets(\'Counter increments smoke test\', (WidgetTester tester) async {\n' \
                                      '    // Build our app and trigger a frame.\n' \
                                      '    await tester.pumpWidget(MyApp());\n\n' \
                                      '    // Verify that our counter starts at 0.\n' \
                                      '    expect(find.text(\'0\'), findsOneWidget);\n' \
                                      '    expect(find.text(\'1\'), findsNothing);\n\n' \
                                      '    // Tap the \'+\' icon and trigger a frame.\n' \
                                      '    await tester.tap(find.byIcon(Icons.add));\n' \
                                      '    await tester.pump();\n\n' \
                                      '    // Verify that our counter has incremented.\n' \
                                      '    expect(find.text(\'0\'), findsNothing);\n' \
                                      '    expect(find.text(\'1\'), findsOneWidget);\n' \
                                      '  });\n}\n'

        file_path: str = 'custom_card_design/test/widget_test.dart'
        _r = self.g.download_repo_file(repo_name=self.repo, owner=self.owner, file_path=file_path,
                                       branch=self.branch)

        self.assertEqual(expected_file_contents, _r.data)

    def test_get_git_ref(self):
        r: GithubRefObject = self.g.get_git_ref(self.owner, self.repo, self.branch)
        expected_res = get(url=f'https://api.github.com/repos/{self.owner}/{self.repo}/git/ref/heads/{self.branch}',
                           headers=self.header)

        if expected_res.status_code != 200:
            self.fail(
                f'Failed test due to following error while running get: {expected_res.status_code} {expected_res.reason}')
        else:
            j = loads(expected_res.text)
            self.assertEqual(r.url, j['url'])
            self.assertEqual(r.nodeId, j['node_id'])
            self.assertEqual(r.ref, j['ref'])
            self.assertEqual(r.obj, j['object'])

    # ## todo:some documentation is causing  404 not found return response for http post. So commenting this test
    #  will #  run after the issue is resolved. refrain for using the function module in original code till then.
    #  def test_post_blob(self): # Data that will be posted to the Github server to create a blob. expected_data =
    #  'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sapien nisi, ' \ 'luctus finibus hendrerit
    #  at, dapibus eget lectus. Curabitur suscipit ex lacus, ut tristique ' \ 'mi egestas quis. Sed id tellus
    #  volutpat, porta velit sit amet, dapibus dolor. Nulla a ' \ 'vestibulum massa, eget finibus felis. Fusce at
    #  volutpat est, vel accumsan mauris. Donec ut ' \ 'aliquam nisl. Class aptent taciti sociosqu ad litora torquent
    #  per conubia nostra, ' \ 'per inceptos himenaeos. Suspendisse gravida, nisl at semper ultricies,
    #  risus ex suscipit ' \ 'orci, porta egestas justo libero in libero. Phasellus ornare nibh nunc,
    #  sit amet convallis ' \ 'nisi ullamcorper sed. Pellentesque iaculis enim augue. Etiam lacus lectus, sodales sit
    #  amet ' \ 'purus nec, semper aliquam turpis. Pellentesque habitant morbi tristique senectus et netus et ' \
    #  'malesuada fames ac turpis egestas. Sed a dapibus neque, vel congue tortor. Mauris at ' \ 'ultrices tellus.
    #  \nDonec dictum at felis et vehicula. Interdum et malesuada fames ac ante ' \ 'ipsum primis in faucibus.
    #  Suspendisse mattis laoreet dolor, vitae laoreet nisi consequat ' \ 'non. Sed quis mauris magna. Fusce varius
    #  ante quis justo suscipit, bibendum rhoncus urna ' \ 'gravida. Pellentesque habitant morbi tristique senectus
    #  et netus et malesuada fames ac ' \ 'turpis egestas. In vel nisl tellus. Duis vitae neque vel eros pellentesque
    #  facilisis. Aenean ' \ 'eget suscipit turpis. ' blob = self.g.post_blob(data=expected_data, owner=self.owner,
    #  repo=self.repo) res = get(url=blob.url, headers=self.header) print(blob.url) if res.status_code != 200:
    #  self.fail( f'Failed test due to following error while running get: {res.status_code} {res.reason}') else: j =
    #  loads(res.text) self.assertEqual(expected_data, j['content'])

    def test_get_latest_commit(self):
        commit = self.g.get_latest_commit(owner=self.owner, repo=self.repo, branch=self.branch)

        # getting the latest reference from the branch.
        ref = get(url=f'https://api.github.com/repos/{self.owner}/{self.repo}/git/ref/heads/{self.branch}',
                  headers=self.header)
        if ref.status_code != 200:
            self.fail(
                f'Failed test due to following error while running get on latest reference: {ref.status_code} {ref.reason}')
        else:
            ref_j = loads(ref.text)

            commit_res = get(url=ref_j['object']['url'], headers=self.header)
            commit_j = loads(commit_res.text)

            self.assertEqual(commit_j['sha'], commit.sha)
            self.assertEqual(commit_j['author'], commit.author)
            self.assertEqual(commit_j['committer'], commit.committer)
            self.assertEqual(commit_j['message'], commit.message)
            self.assertEqual(commit_j['tree'], commit.tree)

    def test_get_tree(self):
        tree = self.g.get_tree(owner=self.owner, repo=self.repo, branch=self.branch)

        # getting the latest reference from the branch.
        ref = get(url=f'https://api.github.com/repos/{self.owner}/{self.repo}/git/ref/heads/{self.branch}',
                  headers=self.header)
        if ref.status_code != 200:
            self.fail(
                f'Failed test due to following error while running get on latest reference: {ref.status_code} {ref.reason}')
        else:
            ref_j = loads(ref.text)

            commit_res = get(url=ref_j['object']['url'], headers=self.header)
            commit_j = loads(commit_res.text)

            actual_tree = get(url=f"{commit_j['tree']['url']}?recursive=1", headers=self.header)
            if actual_tree.status_code != 200:
                self.fail(
                    f'Failed test due to following error while running get on latest ree: {actual_tree.status_code} {actual_tree.reason}')
            else:
                actual_tree_j = loads(actual_tree.text)

                self.assertEqual(actual_tree_j['sha'], tree.sha)
                self.assertEqual(actual_tree_j['url'], tree.url)
                self.assertEqual(actual_tree_j['tree'], tree.tree)

    # def test_update_and_post_tree(self):
    #     expected_contents = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Duis at tellus at urna condimentum mattis pellentesque id. Lobortis elementum nibh tellus molestie nunc non. Vestibulum lectus mauris ultrices ' \
    #                         'eros in. Odio ut sem nulla pharetra. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium. Nam libero justo laoreet sit amet cursus. Amet nulla facilisi morbi tempus iaculis urna. Massa id neque aliquam vestibulum morbi blandit cursus risus at. Mi in nulla ' \
    #                         'posuere sollicitudin aliquam ultrices sagittis orci. Lobortis feugiat vivamus at augue eget arcu dictum. Sit amet consectetur adipiscing elit pellentesque. Tortor posuere ac ut consequat semper viverra nam libero justo. Eu nisl nunc mi ipsum faucibus vitae. Semper ' \
    #                         'feugiat nibh sed pulvinar proin gravida hendrerit. Habitant morbi tristique senectus et netus et. Tempor orci dapibus ultrices in iaculis nunc. Amet risus nullam eget felis eget nunc lobortis mattis. Posuere sollicitudin aliquam ultrices sagittis orci. '
    #
    #     tree = [GitTree(path='custom_card_design/test/change_file_test.txt', tree_type=TreeType.BLOB, content=expected_contents)]
    #     posted_tree = self.g.update_and_post_tree(owner=self.owner, repo=self.repo, branch=self.branch, files=tree)
    #     actual_tree = get(url=f'https://api.github.com/repos/octocat/hello-world/git/trees/{posted_tree.sha}?recursive=1')
    #     if actual_tree.status_code != 200:
    #         self.fail(f'Posted tree with sha: {posted_tree.sha} failed to get due to: {actual_tree.status_code} {actual_tree.reason}')
    #     else:
    #         actual_tree_data = loads(actual_tree.text)['tree']
    #         expected_tree_data = loads(posted_tree.tree)
    #         self.assertEqual(actual_tree_data, expected_tree_data)

    def test_commit_files(self):
        pass


class TestGithubAppApi(TestCase):
    app = GithubAppApi(app_id=environ.get('APP_ID'))

    def test_et_app_installations(self):
        with open('D:/work_src/Medium Coders Asylum/bots/cert2.pem', 'rb') as cert_file:
            _pvt = serialization.load_pem_private_key(data=cert_file.read(), password=None, backend=default_backend)
        actual_list = self.app.get_app_installations()
        cur_time = int(round(datetime.now().timestamp()))
        payload = {"iat": cur_time, "exp": cur_time + (60 * 5), "iss": environ.get("APP_ID")}
        encoded = encode(payload=payload, key=_pvt, algorithm="RS256")
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer " + encoded
        headers["Accept"] = "application/vnd.github.v3+json"

        url = "https://api.github.com/app/installations"
        req = get(url=url, headers=headers)
        if req.status_code != 200:
            self.fail(f'Unable to fetch app installations due to: {req.status_code} {req.text}')
        expected_list = loads(req.text)

        self.assertEqual(len(actual_list), len(expected_list))
        for i in range(len(actual_list)):
            self.assertEqual(actual_list[i].org, expected_list[i]['account']['login'])
            self.assertEqual(actual_list[i].install_id, expected_list[i]['id'])
            self.assertEqual(actual_list[i].acc_tkn_url, expected_list[i]['access_tokens_url'])


if __name__ == '__main__':
    main()
