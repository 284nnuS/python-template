from datetime import datetime
from pydantic import BaseModel


class TokenPayload:
    exp: datetime
    iat: datetime
    sub: str
    scope: str

    def __init__(self, exp: datetime, iat: datetime, sub: str, scope: str):
        self.exp = exp
        self.iat = iat
        self.sub = sub
        self.scope = scope


class Token(BaseModel):
    access_token: str
    type: str = "bearer"
