from pydantic import BaseModel


class ClusterRaftServer(BaseModel):
    """
    {
        "address": "string",
        "id": "string",
        "leader": true,
        "voter": true
    }
    """

    address: str
    id: str
    leader: bool
    voter: bool
