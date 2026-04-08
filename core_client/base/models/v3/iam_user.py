from pydantic import BaseModel
from typing import List, Optional

from . import IamUserAuth, IamUserPolicy


class IamUser(BaseModel):
    """
    {
        "auth": IamUserAuth,
        "name": "string",
        "policies": [IamUserPolicy],
        "superuser": true
    }
    + {
        "alias": "string",
        "created_at": int,
        "updated_at": int,
    }
    """

    auth: IamUserAuth | None = None
    name: str | None = None
    alias: str | None = None
    policies: list[IamUserPolicy] | None = None
    superuser: bool = False
    created_at: int | None = None
    updated_at: int | None = None
