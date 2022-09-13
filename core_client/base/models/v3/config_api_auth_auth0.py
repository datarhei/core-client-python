from pydantic import BaseModel
from typing import Optional, List


class ConfigApiAuthAuth0(BaseModel):
    """
    {
        "enable": False,
        "tenants": []
    }
    """

    enable: Optional[bool]
    tenants: Optional[List[str]]
