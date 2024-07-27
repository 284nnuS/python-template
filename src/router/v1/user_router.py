from fastapi import APIRouter, Depends
from ..dependencies import get_current_user, engine

router = APIRouter()


@router.get("/user/get_me")
def get_me(
    current_user: Depends = Depends(get_current_user),
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    return current_user.serialize()
