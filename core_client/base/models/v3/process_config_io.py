from typing import List, Optional
from pydantic import BaseModel

from . import ProcessConfigIOCleanup


class ProcessConfigIO(BaseModel):
    """
    {
        "address": "http://127.0.0.1:8080/memfs/abc.m3u8",
        "cleanup": [ProcessConfigIOCleanup],
        "id": "input_0",
        "options": [
            "-fflags",
            "+genpts",
            "-thread_queue_size",
            "512",
            "-analyzeduration",
            "20000000",
            "-re"
        ]
    }
    """

    address: str
    cleanup: Optional[List[ProcessConfigIOCleanup]] = None
    id: str
    options: Optional[List[str]] = None
