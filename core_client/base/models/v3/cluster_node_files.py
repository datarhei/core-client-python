from pydantic import BaseModel
from typing import Dict, List


class ClusterNodeFiles(BaseModel):
    """
    {
        "files": {
            "additionalProp1": [
                "string"
            ],
            "additionalProp2": [
                "string"
            ],
            "additionalProp3": [
                "string"
            ]
        },
        "last_update": 0
    }
    """

    files: dict[str, list[str]]
    last_update: int
