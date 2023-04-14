from pydantic import BaseModel


class ProcessStateProgressIOFramerate(BaseModel):
    """
    {
        "avg": 24.999,
        "min": 25,
        "max": 19.531,
    }
    """

    avg: float
    min: float
    max: float
