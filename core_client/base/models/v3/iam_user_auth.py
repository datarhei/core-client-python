from pydantic import BaseModel
from typing import Optional

from . import IamUserAuthApi, IamUserAuthServices


class IamUserAuth(BaseModel):
    """
    {
        "api": IamUserAuthApi,
        "services": {
            "basic": [
                "string"
            ],
            "session": [
                "string"
            ],
            "token": [
                "string"
            ]
        }
    }
    """

    api: Optional[IamUserAuthApi] = None
    services: Optional[IamUserAuthServices] = None
