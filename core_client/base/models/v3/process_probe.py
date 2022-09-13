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

    log: List[str]
    streams: List[ProcessProbeStream]
