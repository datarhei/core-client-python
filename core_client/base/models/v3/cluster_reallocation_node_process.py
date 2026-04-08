from pydantic import BaseModel


class ClusterReallocationNodeProcess(BaseModel):
    """
    {"id": "process1", "domain": "domainX"}
    """

    id: str
    domain: str
