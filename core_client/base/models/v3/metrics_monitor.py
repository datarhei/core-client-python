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

    labels: Union[None, Dict[str, str]]
    name: MetricsMonitorName
    values: Optional[List[List[Union[int, float]]]] = None

    class ConfigDict:
        use_enum_values = True
