from pydantic_collections import BaseCollectionModel

from . import Filesystem


class FilesystemList(BaseCollectionModel[Filesystem]):
    pass
