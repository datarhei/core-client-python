from pydantic import BaseModel

from . import ProcessStateProgressIOAvstreamIOState


class ProcessStateProgressIOAvstreamIO(BaseModel):
    """
    {
        "state": "ProcessStateProgressIOAvstreamIOState",
        "packet": 183818,
        "time": 7335,
        "size_kb": 1801687
    }
    """

    packet: float
    size_kb: float
    state: ProcessStateProgressIOAvstreamIOState
    time: int

    class ConfigDict:
        use_enum_values = True
