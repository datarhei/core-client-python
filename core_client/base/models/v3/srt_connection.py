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

    log: Dict[str, str]
    stats: SrtConnectionStats
