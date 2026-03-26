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
    + {
        "binary": str,
    }
    """

    autostart: bool = True
    id: str
    input: list[ProcessConfigIO]
    limits: ProcessConfigLimit | None = None
    options: list[str]
    output: list[ProcessConfigIO]
    reconnect: bool = True
    reconnect_delay_seconds: int = 60
    reference: str
    stale_timeout_seconds: int = 10
    scheduler: str | None = None
    runtime_duration_seconds: int | None = None
    log_patterns: list[str] | None = None
    type: ProcessConfigType = ProcessConfigType.ffmpeg
    binary: str | None = None
    domain: str | None = None
    owner: str | None = None
    metadata: dict[str, str | dict | list | int | float | bool] | None = None

    class ConfigDict:
        use_enum_values = True
