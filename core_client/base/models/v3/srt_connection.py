from pydantic import BaseModel
from typing import Dict

from . import SrtConnectionStats, SrtLog


class SrtConnection(BaseModel):
    """
    {
        "log": {"<name>": [SrtLog]},
        "stats": SrtConnectionsStats
    }
    """

    log: dict[str, list[SrtLog]] | None = None
    stats: SrtConnectionStats
