from pydantic import BaseModel
from typing import Union, Optional
from . import ProcessStateProgressIOTeeState


class ProcessStateProgressIOTee(BaseModel):
    """
    {
        "id": "out1",
        "address": "http://...,
        "format": "hls",
        "state": "running",
        "fifo_enabled": true,
        "fifo_state": "running",
        "fifo_recovery_attempts_total": 3
    }
    """

    id: Optional[str] = None
    address: str
    format: str
    state: Optional[str] = None  # e.g., "running", "stopped", "error"
    fifo_enabled: bool = False
    fifo_state: Optional[str] = None  # e.g., "running", "stopped", "error"
    fifo_recovery_attempts_total: Optional[int] = None

    class ConfigDict:
        use_enum_values = True
