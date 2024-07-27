from .settings import settings
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
# from typing import str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
        subject: str,
        expires_date: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)):
    expire_at = datetime.utcnow() + expires_date
    issued_at = datetime.utcnow()

    payload = {
        'exp': expire_at + expires_date,
        'iat': issued_at,
        'sub': subject,
        'scope': "access_token"
    }

    encoded_jwt = jwt.encode(
        payload, settings.SECRET_KEY, algorithm=ALGORITHM
    )

    return encoded_jwt


def decode_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])