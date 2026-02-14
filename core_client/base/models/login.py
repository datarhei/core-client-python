from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_at: Optional[int] = None


class AccessToken(BaseModel):
    access_token: str
