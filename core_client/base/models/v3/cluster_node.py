from pydantic import BaseModel

from . import ClusterNodeResources, ClusterNodeCore


class ClusterNode(BaseModel):
    """
    {
        "id": "cluster-node-n1",
        "name": "lucky-lab-7523",
        "version": "1.0.2",
        "status": "online",
        "error": "",
        "voter": True,
        "leader": False,
        "address": "10.0.0.1:8001",
        "created_at": "2023-07-19T15:46:47Z",
        "uptime_seconds": 4541,
        "last_contact_ms": 975.930708,
        "latency_ms": 0.170464,
        "core": ClusterNodeCore,
        "resources": ClusterNodeResources
    }
    """

    id: str
    name: str
    version: str
    status: str
    error: str
    voter: bool
    leader: bool
    address: str
    created_at: str
    uptime_seconds: int
    last_contact_ms: float
    latency_ms: float
    core: ClusterNodeCore
    resources: ClusterNodeResources
