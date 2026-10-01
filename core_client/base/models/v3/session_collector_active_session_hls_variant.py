from pydantic import BaseModel
from typing import Optional


class SessionCollectorActiveSessionHlsVariant(BaseModel):
    """
    {
        "path": "/memfs/.../live/0.m3u8",
        "active": true,
        "switches": 2,
        "bandwidth_bits": 2393600,
        "resolution": "1280x720",
        "codecs": ""
    }
    """

    path: str | None = None
    active: bool | None = None
    switches: int | None = None
    bandwidth_bits: int | None = None
    resolution: str | None = None
    codecs: str | None = None
