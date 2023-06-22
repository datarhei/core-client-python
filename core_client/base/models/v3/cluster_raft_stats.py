from pydantic import BaseModel


class ClusterRaftStats(BaseModel):
    """
    {
        "last_contact_ms": 0,
        "num_peers": 0,
        "state": "string"
    }
    """

    last_contact_ms: int
    num_peers: int
    state: str
