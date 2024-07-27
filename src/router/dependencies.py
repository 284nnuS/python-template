from core.db import engine, get_db
from core.settings import settings
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, status
from sqlalchemy.orm import Session
import jwt
from fastapi import HTTPException
import core.security as security
from model import User
from schemas import TokenPayload
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from service.user_service import UserService

reuseable_oauth_2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access_token"
)

SessionDependency = Annotated[Session, Depends(get_db)]
TokenDependency = Annotated[str, Depends(reuseable_oauth_2)]


def get_current_user(session: SessionDependency, token: TokenDependency) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user_service = UserService(session)
    user = user_service.get_by_name(token_data.sub)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]