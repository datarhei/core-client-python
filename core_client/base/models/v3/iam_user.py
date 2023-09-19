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

    auth: Optional[IamUserAuth]
    name: Optional[str]
    alias: Optional[str]
    policies: Optional[List[IamUserPolicy]]
    superuser: bool = False
    created_at: Optional[int]
    updated_at: Optional[int]
