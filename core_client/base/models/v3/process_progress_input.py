from pydantic import BaseModel
from typing import List, Optional

from . import ProcessProgressInputAvstream


class ProcessProgressInput(BaseModel):
    """
    {
        "avstream": ProcessProgressInputAvstream,
        "bitrate": 0,
        "fps": 0,
        "id": "string",
        "iomap": [0],
        "type": "string"
    }
    """

    avstream: ProcessProgressInputAvstream | None = None
    bitrate: float | None = None
    fps: float | None = None
    id: str | None = None
    iomap: list[int] | None = None
    type: str | None = None
