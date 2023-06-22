from pydantic import BaseModel

from . import ClusterNodeList, ClusterRaft


class Cluster(BaseModel):
    """
    {
        "address": "string",
        "cluster_api_address": "string",
        "core_api_address": "string",
        "degraded": true,
        "degraded_error": "string",
        "id": "string",
        "nodes": [ClusterNode],
        "raft": ClusterRaft,
        "version": "string"
    }
    """

    address: str
    cluster_api_address: str
    core_api_address: str
    degraded: bool
    degraded_error: str
    id: str
    nodes: ClusterNodeList
    raft: ClusterRaft
    version: str
