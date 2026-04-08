from pydantic import BaseModel
from typing import Optional

from . import ConfigApiAccessRules


class ConfigApiAccess(BaseModel):
    """
    {
        "http": ConfigApiAccessRules,
        "https": ConfigApiAccessRules
    }
    """

    http: ConfigApiAccessRules | None = None
    https: ConfigApiAccessRules | None = None
