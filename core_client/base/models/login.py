from pydantic import BaseModel


class Token(BaseModel):
    access_token: str = None
    refresh_token: str = None


class AccessToken(BaseModel):
    access_token: str
