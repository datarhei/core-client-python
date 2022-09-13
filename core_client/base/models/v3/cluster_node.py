from pydantic import BaseModel


class ClusterNode(BaseModel):
    address: str
    id: str
    last_update: int
    state: str
