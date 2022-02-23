from hashlib import sha1
import hmac as crypto
import azure.functions as func
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from jwt import encode


def get_hash_key(key: str, req: func.HttpRequest) -> str:
    _hmac_hashed = crypto.new(key=bytes(key), msg=req.get_body, digestmod=sha1)
    return _hmac_hashed.digest().encode("base64").rstrip('\n')


def generate_jwt_token(payload: dict) -> str:
    file_path: str = 'D:/work_src/Medium Coders Asylum/bots/cert2.pem'
    pwd: str = None
    with open(file_path, 'rb') as file:
        _pvt_key = serialization.load_pem_private_key(data=file.read(), password=pwd, backend=default_backend)
    return encode(payload=payload, key=_pvt_key, algorithm='RS256')


if __name__ == '__main__':
    pass

