from pydantic import BaseModel
from typing import List, Optional


class ProcessProgressOutput(BaseModel):
    """
    {
        "bitrate": 0,
        "fps": 0,
        "id": "string",
        "iomap": [0],
        "q": 0,
        "type": "string"
    }
    """

    bitrate: float | None = None
    fps: float | None = None
    id: str | None = None
    iomap: list[int] | None = None
    q: float | None = None
    type: str | None = None
