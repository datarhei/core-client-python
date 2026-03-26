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

    read_only: bool | None = None
    access: ConfigApiAccess | None = None
    auth: ConfigApiAuth | None = None
