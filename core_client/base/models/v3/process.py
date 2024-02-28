from pydantic import BaseModel
from typing import Dict, Optional

from . import ProcessConfigType, ProcessConfig, ProcessReport, ProcessState


class Process(BaseModel):
    """
    {
        "config": ProcessConfig,
        "created_at": "2022-07-27T12:00:49+00:00",
        "id": "restreamer-ui:ingest:c9e4b64b-5491-455f-b7ee-6b47d8842f74",
        "metadata": null,
        "reference": "c9e4b64b-5491-455f-b7ee-6b47d8842f74",
        "state": ProcessState,
        "report": ProcessReport,
        "type": ProcessConfigType
    }
    """

    """
    + {
        "updated_at": "2022-07-27T12:00:49+00:00",
        "domain": str,
        "owner": str,
        "core_id": str,
    }
    """

    config: Optional[ProcessConfig] = None
    created_at: int
    id: str
    metadata: Optional[Dict] = None
    reference: str
    state: Optional[ProcessState] = None
    report: Optional[ProcessReport] = None
    type: ProcessConfigType
    updated_at: Optional[int] = None
    domain: Optional[str] = None
    owner: Optional[str] = None
    core_id: Optional[str] = None

    class ConfigDict:
        use_enum_values = True
