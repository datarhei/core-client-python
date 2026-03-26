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

    cpu_usage: ProcessStateResourcesCpuUsage | None = None
    memory_bytes: ProcessStateResourcesMemoryBytes | None = None
    gpu: ProcessStateResourcesGpu | None = None
