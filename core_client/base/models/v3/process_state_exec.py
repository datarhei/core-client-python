from enum import Enum


class ProcessStateExec(str, Enum):
    """
    "exec": "finished",
    """

    finished = "finished"
    running = "running"
    starting = "starting"
    finishing = "finishing"
    failed = "failed"
    killed = "killed"
