from pydantic import BaseModel, Field

class LoginInput(BaseModel):
    username: str = Field('<USERNAME>')
    password: str = Field('<PASSWORD>')