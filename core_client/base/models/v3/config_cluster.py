from pydantic import BaseModel
from typing import Optional


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
    debug: Optional[bool] = None
    emergency_leader_timeout_sec: Optional[int] = None
    enable: Optional[bool] = None
    node_recover_timeout_sec: Optional[int] = None
    peers: Optional[list[str]] = None
    sync_interval_sec: Optional[int] = None
