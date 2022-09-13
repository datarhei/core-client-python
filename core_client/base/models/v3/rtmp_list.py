from pydantic_collections import BaseCollectionModel

from . import Rtmp


class RtmpList(BaseCollectionModel[Rtmp]):
    pass
