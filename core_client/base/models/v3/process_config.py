from pydantic import BaseModel
from typing import List, Optional, Union

from . import ProcessConfigIO, ProcessConfigLimit, ProcessConfigType


class ProcessConfig(BaseModel):
    """
    {
        "autostart": true,
        "id": "abc",
        "input": [ProcessConfigIO],
        "limits": {ProcessConfigLimit},
        "options": [
            "-err_detect",
            "ignore_err"
        ],
        "output": [ProcessConfigIO],
        "reconnect": true,
        "reconnect_delay_seconds": 15,
        "reference": "c9e4b64b-5491-455f-b7ee-6b47d8842f74",
        "stale_timeout_seconds": 30,
        "type": "ProcessConfigType"
    }
    """

    """
    v16.13.0
    {
        "scheduler": str,
        "runtime_duration_seconds": int,
        "log_pattern": [str]
    }
    """
    """
    + {
        "domain": str,
        "owner": str,
        "metadata": {"key": {...}},
    }
    """

    autostart: bool = True
    id: str
    input: List[ProcessConfigIO]
    limits: Optional[ProcessConfigLimit] = None
    options: List[str]
    output: List[ProcessConfigIO]
    reconnect: bool = True
    reconnect_delay_seconds: int = 60
    reference: str
    stale_timeout_seconds: int = 10
    scheduler: Optional[str] = None
    runtime_duration_seconds: Optional[int] = None
    log_patterns: Optional[List[str]] = None
    type: ProcessConfigType = ProcessConfigType.ffmpeg
    domain: Optional[str] = None
    owner: Optional[str] = None
    metadata: Optional[dict[str, Union[str, dict, list, int, float, bool]]] = None

    class ConfigDict:
        use_enum_values = True
