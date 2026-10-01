from pydantic import BaseModel
from typing import Dict, List, Optional

from . import (
    SessionCollectorActiveSessionHlsBandwidth,
    SessionCollectorActiveSessionHlsSegments,
    SessionCollectorActiveSessionHlsVariant,
)


class SessionCollectorActiveSessionHls(BaseModel):
    """
    {
        "hls_variants": [SessionCollectorActiveSessionHlsVariant],
        "hls_segments": SessionCollectorActiveSessionHlsSegments,
        "http_status": {
            "200": 2954
        },
        "bandwidth_tx_bits": SessionCollectorActiveSessionHlsBandwidth
    }
    """

    hls_variants: list[SessionCollectorActiveSessionHlsVariant] | None = None
    hls_segments: SessionCollectorActiveSessionHlsSegments | None = None
    http_status: dict[str, int] | None = None
    bandwidth_tx_bits: SessionCollectorActiveSessionHlsBandwidth | None = None
