from pydantic import BaseModel, RootModel

from . import ReportProcess


class ReportProcessList(BaseModel):
    """
    [{
        "created_at": 0,
        "exit_state": "string",
        "id": "string",
        "reference": "string"
    }]
    """

    RootModel: ReportProcess
