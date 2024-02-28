from pydantic import BaseModel
from typing import Optional

from . import ConfigApiAccess, ConfigApiAuth


class ConfigApi(BaseModel):
    """
    {
        "read_only": False,
        "access": ConfigApiAccess,
        "auth": ConfigApiAuth
    }
    """

    read_only: Optional[bool] = None
    access: Optional[ConfigApiAccess] = None
    auth: Optional[ConfigApiAuth] = None
