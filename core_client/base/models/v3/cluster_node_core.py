from pydantic import BaseModel


class ClusterNodeCore(BaseModel):
    """
    {
        "address": "http://10.0.10.1:80/",
        "status": "online",
        "error": "",
        "last_contact_ms": 975.321866,
        "latency_ms": 0.452108
    }
    """

    address: str
    status: str
    error: str
    last_contact_ms: float
    latency_ms: float
