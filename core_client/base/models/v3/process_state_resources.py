from pydantic import BaseModel
from typing import Optional

from . import ProcessStateResourcesCpuUsage, ProcessStateResourcesMemoryBytes


class ProcessStateResources(BaseModel):
    """
    {
        "cpu_usage": ProcessStateResourcesCpuUsage,
        "memory_bytes": ProcessStateResourcesMemoryBytes
    }
    """

    cpu_usage: Optional[ProcessStateResourcesCpuUsage]
    memory_bytes: Optional[ProcessStateResourcesMemoryBytes]
