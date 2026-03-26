from pydantic import BaseModel
from typing import Optional


class ProcessStateResourcesCpuUsage(BaseModel):
    """
    {
        "avg": 0,
        "cur": 0,
        "limit": 0,
        "max": 0,
        "ncpu": 0
        + "throttling": false
    }
    """

    avg: float | None = None
    cur: float | None = None
    limit: float | None = None
    max: float | None = None
    ncpu: float | None = None
    throttling: bool | None = None
