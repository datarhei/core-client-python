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
    debug: Optional[bool]
    emergency_leader_timeout_sec: Optional[int]
    enable: Optional[bool]
    node_recover_timeout_sec: Optional[int]
    peers: Optional[list[str]]
    sync_interval_sec: Optional[int]
