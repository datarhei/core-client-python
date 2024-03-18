from pydantic import BaseModel, RootModel

from . import Filesystem


class FilesystemList(BaseModel):
    RootModel: Filesystem
