from pydantic import BaseModel, RootModel

from . import FilesystemFile


class FilesystemFileList(BaseModel):
    RootModel: FilesystemFile
