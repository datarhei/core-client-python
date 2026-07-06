from pydantic import RootModel

from . import Rtmp

# JSON array of Rtmp.
RtmpList = RootModel[list[Rtmp]]
