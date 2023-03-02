from pydantic_collections import BaseCollectionModel

from . import ReportProcess


class ReportProcessList(BaseCollectionModel[ReportProcess]):
    """
    [{
        "created_at": 0,
        "exit_state": "string",
        "id": "string",
        "reference": "string"
    }]
    """

    pass
