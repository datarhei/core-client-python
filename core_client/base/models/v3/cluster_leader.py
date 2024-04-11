from pydantic import BaseModel


class ClusterLeader(BaseModel):
    """
    {
        "address": "10.196.88.9:8000",
        "elected_seconds": 514,
        "id": "core1"
    }
    """

    address: str
    elected_seconds: int
    id: str
