from pydantic import BaseModel
from typing import List

from . import ProcessProbeStream


class ProcessProbe(BaseModel):
    """
    {
        "log": [
            "string"
        ],
        "streams": [ProcessProbeStream]
    }
    """

    log: list[str]
    streams: list[ProcessProbeStream]
