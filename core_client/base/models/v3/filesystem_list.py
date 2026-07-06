from pydantic import RootModel

from . import Filesystem

# JSON array of Filesystem.
FilesystemList = RootModel[list[Filesystem]]
