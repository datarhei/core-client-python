from pydantic import BaseModel


class ClusterRaft(BaseModel):
    """
    {
        "address": "10.0.0.1:8000",
        "state": "Follower",
        "last_contact_ms": 28.782888,
        "num_peers": 1,
        "log_term": 873,
        "log_index": 1949
    }
    """

    address: str
    state: str
    last_contact_ms: float
    num_peers: int
    log_term: int
    log_index: int
