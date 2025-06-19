from enum import Enum


class ProcessStateProgressIOTeeState(str, Enum):
    """
    "state": "running"
    """

    running = "running"
    failed = "failed"
    restart = "restart"
