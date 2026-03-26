from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None
    expires_at: int | None = None


class AccessToken(BaseModel):
    access_token: str
