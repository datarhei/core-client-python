from pydantic import BaseModel

from . import ClusterNode, ClusterRaft


class Cluster(BaseModel):
    """
    {
        "id": "cluster-node-1",
        "name": "lucky-lab-7523",
        "leader": False,
        "address": "10.0.0.1:8001",
        "nodes": [ClusterNode],
        "raft": ClusterRaft,
        "version": "1.0.2",
        "degraded": False,
        "degraded_error": ""
    }
    """

    id: str
    name: str
    leader: bool
    address: str
    raft: ClusterRaft
    nodes: list[ClusterNode]
    version: str
    degraded: bool
    degraded_error: str
