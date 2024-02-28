from pydantic import BaseModel
from typing import Optional


class ProcessStateResourcesMemoryBytes(BaseModel):
    """
        {
            "avg": 0,
            "cur": 0,
            "limit": 0,
            "max": 0
    }
    """

    avg: Optional[float] = None
    cur: Optional[float] = None
    limit: Optional[float] = None
    max: Optional[float] = None
