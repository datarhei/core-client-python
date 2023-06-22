from pydantic import BaseModel
from typing import Optional


class ConfigResources(BaseModel):
    """
    {
        "max_cpu_usage": float,
        "max_memory_usage": float,
    }
    """

    max_cpu_usage: Optional[float]
    max_memory_usage: Optional[float]
