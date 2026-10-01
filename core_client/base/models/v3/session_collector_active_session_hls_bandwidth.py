from pydantic import BaseModel
from typing import Optional


class SessionCollectorActiveSessionHlsBandwidth(BaseModel):
    """
    {
        "min": 20901924.340143416,
        "max": 2540419186.6611648,
        "avg": 1001351629.3989341
    }
    """

    min: float | None = None
    max: float | None = None
    avg: float | None = None
