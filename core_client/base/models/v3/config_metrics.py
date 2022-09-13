from pydantic import BaseModel
from typing import Optional


class ConfigMetrics(BaseModel):
    """
    {
        "enable": True,
        "enable_prometheus": False,
        "range_sec": 300,
        "interval_sec": 2
    }
    """

    enable: Optional[bool]
    enable_prometheus: Optional[bool]
    range_sec: Optional[int]
    interval_sec: Optional[int]
