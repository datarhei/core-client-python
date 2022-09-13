from pydantic_collections import BaseCollectionModel

from . import FilesystemFile


class FilesystemFileList(BaseCollectionModel[FilesystemFile]):
    pass
