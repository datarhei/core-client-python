from pydantic import BaseModel


class ClusterNodeResources(BaseModel):
    """
    {
        "cpu_limit": 0,
        "cpu_used": 0,
        "is_throttling": true,
        "memory_limit_bytes": 0,
        "memory_used_bytes": 0,
        "ncpu": 0
    }
    """

    cpu_limit: float
    cpu_used: float
    is_throttling: bool
    memory_limit_bytes: int
    memory_used_bytes: int
    ncpu: float
