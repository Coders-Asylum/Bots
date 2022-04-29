from unittest import main, TestCase

from lib.data import GithubAppApiException, GithubApiException, ExceptionType
from lib.data.constants import Status
from lib.handlers import Response


class AppException_tests(TestCase):
    st = Status()

    def raise_appApiException(self):
        raise GithubAppApiException(msg='Test message', response=Response(status_code=self.st.program_error['status_code'], status=self.st.program_error['status'], data='{message: test error}'), api='test api', error_type=ExceptionType.WARNING)

    def raise_apiException(self):
        raise GithubApiException(msg='Test message', response=Response(status_code=self.st.program_error['status_code'], status=self.st.program_error['status'], data='{message: test error}'), api='test api', error_type=ExceptionType.WARNING)

    def test_GithubAppApiException(self):
        with self.assertRaises(GithubAppApiException) as error_context:
            self.raise_appApiException()

        self.assertEqual(error_context.exception.response.data, '{message: test error}')
        self.assertEqual(error_context.exception.response.status_code, self.st.program_error['status_code'])
        self.assertEqual(error_context.exception.response.status, self.st.program_error['status'])

    def test_GithubApiException(self):
        with self.assertRaises(GithubApiException) as error_context:
            self.raise_apiException()

        self.assertEqual(error_context.exception.response.data, '{message: test error}')
        self.assertEqual(error_context.exception.response.status_code, self.st.program_error['status_code'])
        self.assertEqual(error_context.exception.response.status, self.st.program_error['status'])


if __name__ == '__main__':
    main()
