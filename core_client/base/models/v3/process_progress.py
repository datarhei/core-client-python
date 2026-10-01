from pydantic import BaseModel
from typing import List, Optional

from . import ProcessProgressInput, ProcessProgressOutput


class ProcessProgress(BaseModel):
    """
    The progress payload of a process event. This is the compact form sent on
    the process event streams - not to be confused with ProcessStateProgress,
    the full progress of GET /api/v3/process/{id}/state.

    {
        "input": [ProcessProgressInput],
        "output": [ProcessProgressOutput],
        "speed": 0,
        "time": 0
    }
    """

    input: list[ProcessProgressInput] | None = None
    output: list[ProcessProgressOutput] | None = None
    speed: float | None = None
    time: float | None = None
