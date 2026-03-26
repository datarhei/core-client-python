from pydantic import BaseModel
from typing import Dict

from . import SrtConnectionStats


class SrtConnection(BaseModel):
    """
    {
        "log": {},
        "stats": SrtConnectionsStats
    }
    """

    log: dict[str, str]
    stats: SrtConnectionStats
