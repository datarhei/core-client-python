from pydantic import BaseModel
from typing import Optional

from . import ProcessStateResourcesCpuUsage, ProcessStateResourcesMemoryBytes, ProcessStateResourcesGpu


class ProcessStateResources(BaseModel):
    """
    {
        "cpu_usage": ProcessStateResourcesCpuUsage,
        "memory_bytes": ProcessStateResourcesMemoryBytes
    }
    """

    cpu_usage: Optional[ProcessStateResourcesCpuUsage] = None
    memory_bytes: Optional[ProcessStateResourcesMemoryBytes] = None
    gpu: Optional[ProcessStateResourcesGpu] = None
