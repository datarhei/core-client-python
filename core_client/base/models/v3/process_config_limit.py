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

    + {
        "log_event_rate": 100
    }
    """

    cpu_usage: float | None = 0
    memory_mbytes: int | None = 0
    gpu_usage: float | None = 0
    gpu_encoder: float | None = 0
    gpu_decoder: float | None = 0
    gpu_memory_mbytes: int | None = 0
    waitfor_seconds: int | None = 0
    log_event_rate: float | None = 0
