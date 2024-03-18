from pydantic import BaseModel, RootModel

from . import Rtmp


class RtmpList(BaseModel):
    RootModel: list[Rtmp]
