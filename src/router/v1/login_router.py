from core import security
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from router.dependencies import SessionDependency, CurrentUser
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from service.user_service import UserService
from schemas.login_schema import LoginInput
from schemas.token_schema import Token
from core.security import create_access_token

router = APIRouter()


@router.post("/login/access_token")
def login_access_token(
    session: SessionDependency,
    login_input: Annotated[OAuth2PasswordRequestForm, Depends()]
)-> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user_service = UserService(session)
    user = user_service.authenticate(login_input.username, login_input.password)
    if not user:
        raise HTTPException(status_code=404, detail="Incorect username or password")
    return Token(
        access_token=create_access_token(user.name)
    )

