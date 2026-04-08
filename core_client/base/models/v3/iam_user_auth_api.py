from pydantic import BaseModel
from typing import Optional

from . import IamUserAuthApiAuth0


class IamUserAuthApi(BaseModel):
    """
    {
        "auth0": IamUserAuthApiAuth0,
        "userpass": "string"
    }
    """

    auth0: IamUserAuthApiAuth0 | None = None
    userpass: str | None = None
