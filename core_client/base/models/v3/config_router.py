from pydantic import BaseModel
from typing import Optional, List


class ConfigRouter(BaseModel):
    """
    {
        "blocked_prefixes": ["/api"],
        "routes": {},
        "ui_path": "/core/ui"
    }
    """

    blocked_prefixes: Optional[List[str]]
    routes: Optional[dict]
    ui_path: Optional[str]
