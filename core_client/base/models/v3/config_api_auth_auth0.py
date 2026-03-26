from pydantic import BaseModel
from typing import Optional, List

from . import ConfigApiAuthAuth0Tenant


class ConfigApiAuthAuth0(BaseModel):
    """
    {
        "enable": False,
        "tenants": []
    }
    """

    enable: bool | None = None
    tenants: list[ConfigApiAuthAuth0Tenant] | None = None
