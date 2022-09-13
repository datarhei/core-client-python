from pydantic import BaseModel
from typing import List, Optional

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

    autostart: bool = True
    id: str
    input: List[ProcessConfigIO]
    limits: Optional[ProcessConfigLimit]
    options: List[str]
    output: List[ProcessConfigIO]
    reconnect: bool = True
    reconnect_delay_seconds: int = 60
    reference: str
    stale_timeout_seconds: int = 10
    type: ProcessConfigType = ProcessConfigType.ffmpeg

    class Config:
        use_enum_values = True
