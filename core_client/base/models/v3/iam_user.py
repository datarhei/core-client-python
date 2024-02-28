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

    auth: Optional[IamUserAuth] = None
    name: Optional[str] = None
    alias: Optional[str] = None
    policies: Optional[List[IamUserPolicy]] = None
    superuser: bool = False
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
