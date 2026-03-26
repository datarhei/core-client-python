from pydantic import BaseModel
from typing import Optional

from . import ProcessStateResourcesGpuEncoder, ProcessStateResourcesGpuDecoder, ProcessStateResourcesGpuUsage, ProcessStateResourcesGpuMemoryBytes, ProcessStateResourcesGpuUsage

class ProcessStateResourcesGpu(BaseModel):
    """
    {
      "decoder": {ProcessStateResourcesGpuDecoder},
      "encoder": {ProcessStateResourcesGpuEncoder},
      "index": -1,
      "memory_bytes": {ProcessStateResourcesGpuMemoryBytes},
      "usage": {ProcessStateResourcesGpuUsage}
    }
    """

    decoder: ProcessStateResourcesGpuDecoder | None = None
    encoder: ProcessStateResourcesGpuEncoder | None = None
    index: int | None = None
    memory_bytes: ProcessStateResourcesGpuMemoryBytes | None = None
    usage: ProcessStateResourcesGpuUsage | None = None
