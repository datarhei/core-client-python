from pydantic import BaseModel
from typing import Optional


class ClusterNodeResourcesGpu(BaseModel):
    """
    api.ClusterNodeGPUResources

    {
        "memory_limit_bytes": 0,
        "memory_total_bytes": 0,
        "memory_used_bytes": 0,
        "usage_decoder": 0,
        "usage_encoder": 0,
        "usage_general": 0,
        "usage_limit": 0
    }
    """

    memory_limit_bytes: int | None = None
    memory_total_bytes: int | None = None
    memory_used_bytes: int | None = None
    usage_decoder: float | None = None
    usage_encoder: float | None = None
    usage_general: float | None = None
    usage_limit: float | None = None
