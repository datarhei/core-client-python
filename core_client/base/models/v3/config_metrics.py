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

    enable: bool | None = None
    enable_prometheus: bool | None = None
    range_sec: int | None = None
    interval_sec: int | None = None
