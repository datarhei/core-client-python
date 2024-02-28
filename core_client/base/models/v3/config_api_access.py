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

    http: Optional[ConfigApiAccessRules] = None
    https: Optional[ConfigApiAccessRules] = None
