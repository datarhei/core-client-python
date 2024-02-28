from pydantic import BaseModel, model_validator
from typing import Dict, Union, List, Optional

from . import SrtConnection


class Srt(BaseModel):
    """
    {
        "name": "936718e2-1226-41f5-a2fe-a965b0187585",
        "socketid": 347916646,
        "subscriber": [417977058],
        "connections": {
            "132881": {SrtConnection}
        },
        "log": {}
    }

    # Deprecated since v16.10.0:
    {
        "publisher": {
            "1f33d538-d714-4c7e-9559-46ddb8118f03": 132881
        },
        "subscriber": {
            "5f61d80a-7aab-4df6-8027-1d4610b814ef": [140529]
        },
        "connections": {
            "132881": {SrtConnection}
        },
        "log": {}
    }
    """

    name: Optional[str] = None
    socketid: Optional[str] = None
    publisher: Optional[Dict[str, int]] = None
    subscriber: Union[Dict[str, List[int]], List[int]]
    connections: Dict[str, SrtConnection]
    log: Union[None, Dict[str, str]]

    @model_validator(mode="before")
    def remove_empty(cls, values):
        if values["name"] is None:
            values.pop("name")
            values.pop("socketid")
        else:
            values.pop("publisher")
        return values
