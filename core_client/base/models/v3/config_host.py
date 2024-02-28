from pydantic import BaseModel
from typing import Optional, List


class ConfigHost(BaseModel):
    """
    {
        "name": ["86.103.229.239"],
        "auto": True
    }
    """

    name: Optional[List[str]] = None
    auto: Optional[bool] = None
