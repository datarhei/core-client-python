from pydantic import BaseModel, Dict, List
from typing import Optional


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

    extras: Optional[Dict[str, Dict]]
    match: Optional[str]
    remote: Optional[List[str]]
    token: Optional[str]
