from pydantic import BaseModel
from typing import Optional, List

from . import Config


class ConfigSaved(BaseModel):
    """
    {
        "created_at": "2022-09-07T19:18:06.320318744Z",
        "loaded_at": "2022-09-07T19:18:06.320318387Z",
        "updated_at": "2022-09-07T19:18:06.320318387Z",
        "config": Config,
        "overrides": [
            "db.dir", "storage.disk.dir", "metrics.enable", "router.ui_path"
        ]
    }
    """

    created_at: Optional[str]
    loaded_at: Optional[str]
    updated_at: Optional[str]
    config: Optional[Config]
    overrides: Optional[List[str]]
