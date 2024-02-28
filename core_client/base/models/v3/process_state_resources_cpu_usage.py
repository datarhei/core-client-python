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

    avg: Optional[float] = None
    cur: Optional[float] = None
    limit: Optional[float] = None
    max: Optional[float] = None
    ncpu: Optional[float] = None
    throttling: Optional[bool] = None
