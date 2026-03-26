from pydantic import BaseModel
from typing import List, Optional, Union, Dict

from . import MetricsMonitorName


class MetricsMonitor(BaseModel):
    """
    {
        "labels": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
        },
        "name": MetricsDataName,
        "values": [[1662502375, 2621939712]]
    }
    """

    labels: None | dict[str, str] | None = None
    name: MetricsMonitorName
    values: list[list[int | float]] | None = None

    class ConfigDict:
        use_enum_values = True
