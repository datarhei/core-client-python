from pydantic import BaseModel

from . import ClusterNodeResources


class ClusterNode(BaseModel):
    """
    {
        "address": "string",
        "created_at": "string",
        "id": "string",
        "last_contact": 0,
        "latency_ms": 0,
        "name": "string",
        "resources": ClusterNodeResources,
        "state": "string",
        "uptime_seconds": 0
    }
    """

    address: str
    created_at: str
    id: str
    last_contact: int
    latency_ms: int
    name: str
    resources: ClusterNodeResources
    state: str
    uptime_seconds: int
