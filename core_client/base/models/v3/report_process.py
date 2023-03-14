from pydantic import BaseModel

from . import ProcessStateExec


class ReportProcess(BaseModel):
    """
    {
        "id": "string",
        "reference": "string",
        "exit_state": "string",
        "created_at": 0,
        "exited_at": 0,
    }
    """

    id: str
    reference: str
    exit_state: ProcessStateExec
    created_at: int
    exited_at: int
