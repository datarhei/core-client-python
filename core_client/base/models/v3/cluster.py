from pydantic import BaseModel
from typing import Union, Optional, List

from . import ClusterNode, ClusterRaft, ClusterLeader


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
    423e0453: {
        "leader": ClusterLeader,
        "public_domains": ["cluster.hardbruecke.ch"],
        "status": "online",
    }
    """

    id: str
    name: Optional[str] = None
    leader: Union[bool, ClusterLeader]
    public_domains: Optional[List[str]] = None
    address: Optional[str] = None
    raft: ClusterRaft
    nodes: list[ClusterNode]
    version: str
    degraded: bool
    degraded_error: str
    status: str
    