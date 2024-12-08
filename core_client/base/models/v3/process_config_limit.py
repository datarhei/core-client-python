from typing import Optional
from pydantic import BaseModel


class ProcessConfigLimit(BaseModel):
    """
    {
        "cpu_usage": 0,
        "memory_mbytes": 0,
        "waitfor_seconds": 0
    }
    
    + {
        "gpu_usage": 100,
        "gpu_encoder": 100,
        "gpu_decoder": 100,
        "gpu_memory_mbytes": 2048
    }
    """

    cpu_usage: Optional[float] = 0
    memory_mbytes: Optional[int] = 0
    gpu_usage: Optional[float] = 0
    gpu_encoder: Optional[float] = 0
    gpu_decoder: Optional[float] = 0
    gpu_memory_mbytes: Optional[int] = 0
    waitfor_seconds: Optional[int] = 0
