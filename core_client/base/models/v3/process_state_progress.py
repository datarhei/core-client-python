from typing import List, Optional
from pydantic import BaseModel

from . import ProcessStateProgressIO, ProcessStateProgressMapping


class ProcessStateProgress(BaseModel):
    """
    {
        "bitrate_kbit": 1970.133,
        "drop": 0,
        "dup": 0,
        "fps": 24.533,
        "frame": 2252071,
        "inputs": [ProcessStateProgressIO],
        "outputs": [ProcessStateProgressIO],
        "packet": 2252071,
        "q": -1,
        "size_kb": 22584958,
        "speed": 1,
        "time": 90082
    }
    """

    bitrate_kbit: float
    drop: int
    dup: int
    fps: float
    frame: int
    inputs: List[ProcessStateProgressIO]
    outputs: List[ProcessStateProgressIO]
    mapping: Optional[ProcessStateProgressMapping] = None
    packet: int
    q: float
    size_kb: int
    speed: float
    time: float
