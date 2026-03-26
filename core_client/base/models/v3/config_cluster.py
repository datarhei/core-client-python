from pydantic import BaseModel
from typing import Optional

from . import ConfigClusterDebug


class ConfigCluster(BaseModel):
    """
    {
        "address": "string",
        "debug": true,
        "emergency_leader_timeout_sec": 0,
        "enable": true,
        "node_recover_timeout_sec": 0,
        "peers": [
            "string"
        ],
        "sync_interval_sec": 0
    }
    """

    address: str
    debug: ConfigClusterDebug
    emergency_leader_timeout_sec: int | None = None
    enable: bool | None = None
    node_recover_timeout_sec: int | None = None
    peers: list[str] | None = None
    sync_interval_sec: int | None = None
