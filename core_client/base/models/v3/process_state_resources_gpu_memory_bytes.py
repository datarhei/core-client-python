from pydantic import BaseModel
from typing import Optional


class ProcessStateResourcesGpuMemoryBytes(BaseModel):
    """
    {
        "avg": 0,
        "cur": 0,
        "limit": 0,
        "max": 0
    }
    """

    avg: float | None = None
    cur: float | None = None
    limit: float | None = None
    max: float | None = None
