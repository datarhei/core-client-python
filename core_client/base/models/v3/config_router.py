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

    blocked_prefixes: list[str] | None = None
    routes: dict | None = None
    ui_path: str | None = None
