from enum import Enum
from pydantic import BaseModel


class ProcessCommandAction(str, Enum):
    start = "start"
    stop = "stop"
    restart = "restart"
    reload = "reload"


class ProcessCommand(BaseModel):
    command: ProcessCommandAction

    class ConfigDict:
        use_enum_values = True
