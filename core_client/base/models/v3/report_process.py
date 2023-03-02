from pydantic import BaseModel

from . import ProcessStateExec


class ReportProcess(BaseModel):
    """
    {
        "created_at": 0,
        "exit_state": "string",
        "id": "string",
        "reference": "string"
    }
    """

    created_at: str
    exit_state: ProcessStateExec
    id: str
    reference: str
