import base64
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from remindme import display

def _build_key_with_password(password: str)-> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        # Constant salt as this isn't getting stored in a DB
        salt=b"pink_himalayan_salt",
        iterations=2000000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt(data: bytes, password: str):
    key = _build_key_with_password(password)
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(data: bytes, password: str):
    try:
        key = _build_key_with_password(password)
        f = Fernet(key)
        return f.decrypt(data)
    except InvalidToken as e:
        display.log_password_issue()
        raise e
