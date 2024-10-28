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

    decoder: Optional[ProcessStateResourcesGpuDecoder] = None
    encoder: Optional[ProcessStateResourcesGpuEncoder] = None
    index: Optional[int] = None
    memory_bytes: Optional[ProcessStateResourcesGpuMemoryBytes] = None
    usage: Optional[ProcessStateResourcesGpuUsage] = None
