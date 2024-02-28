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

    enable: Optional[bool] = None
    tenants: Optional[List[ConfigApiAuthAuth0Tenant]] = None
