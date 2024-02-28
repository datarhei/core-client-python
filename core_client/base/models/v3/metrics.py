from pydantic import BaseModel
from typing import List, Optional

from . import MetricsMonitor


class Metrics(BaseModel):
    """
    {
        "interval_sec": 0,
        "metrics": [MetricsData],
        "timerange_sec": 0
    }
    """

    interval_sec: Optional[int] = None
    metrics: List[MetricsMonitor]
    timerange_sec: Optional[int] = None
