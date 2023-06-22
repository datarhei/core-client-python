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
    """

    auth: Optional[IamUserAuth]
    name: str
    policies: Optional[List[IamUserPolicy]]
    superuser: bool = False
