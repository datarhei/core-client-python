from typing import Optional
from pydantic import BaseModel


class ProcessConfigLimit(BaseModel):
    """
    {
        "cpu_usage": 0,
        "memory_mbytes": 0,
        "waitfor_seconds": 0
    }
    """

    cpu_usage: Optional[float] = 0
    memory_mbytes: Optional[int] = 0
    waitfor_seconds: Optional[int] = 0
