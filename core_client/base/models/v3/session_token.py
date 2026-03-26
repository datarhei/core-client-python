from pydantic import BaseModel
from typing import Optional, Dict, List


class SessionToken(BaseModel):
    """
    {
        "extra": {
            "additionalProp1": {}
        },
        "match": "string",
        "remote": [
            "string"
        ],
        "token": "string"
    }
    """

    match: str = "/**"
    ttl_sec: int = 3600
    extras: dict[str, dict] | None = None
    remote: list[str] | None = None
    token: str | None = None
