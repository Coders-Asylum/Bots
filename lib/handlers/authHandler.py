from hashlib import sha1
import hmac as crypto
import azure.functions as func
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from jwt import encode
from json import loads
from datetime import datetime
from os import environ


def get_hash_key(key: str, req: func.HttpRequest) -> str:
    _hmac_hashed = crypto.new(key=bytes(key), msg=req.get_body, digestmod=sha1)
    return _hmac_hashed.digest().encode("base64").rstrip('\n')


def generate_jwt_token(payload: dict) -> str:
    key: str = environ.get('AUTH_KEY')
    key_bytes: bytes = bytes(key, 'UTF-8')
    _pvt_key = serialization.load_pem_private_key(data=key_bytes, password=None, backend=default_backend)
    return encode(payload=payload, key=_pvt_key, algorithm='RS256')


class GithubAccessToken:
    """
    Github access token to authenticate as the app while interacting with Github APIs
    """
    access_tkn: str
    _time: datetime
    repos: list[str]
    permissions: dict[str, str]

    def __init__(self, data: str):
        _j = loads(data)
        self.access_tkn = _j['token']
        self._time = datetime.strptime(_j['expires_at'], '%Y-%m-%dT%H:%M:%SZ')
        self.permissions = _j['permissions']
        self.__strip_repo_names(repos=_j['repositories'])

    def __strip_repo_names(self, repos: list[dict]) -> None:
        """ Gets only the repository name from the list of repository data used for a check process if required.\

        Args:
            repos (list[dict]): The repositories json object list from the http response.

        Returns: None
        """
        self.repos = []
        for repo in repos:
            self.repos.append(repo['name'])

    def check_exp_time(self) -> bool:
        """Checks if the access token has expired. compares it with the current time.
        Use this before the access token is used and if expired then generate a new token before http call using this token.

        Returns (bool): True if the time is expired, False if access token time in not expired.


        """
        curr_time: datetime = datetime.utcnow()
        if self._time < curr_time:
            return True
        else:
            return False

    def time_of_expire(self) -> datetime:
        """ Time of expiration of the token which is in UTC

        Returns (datetime): datetime object in UTC

        """
        return self._time


if __name__ == '__main__':
    pass
