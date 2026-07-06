from pydantic import RootModel

from . import FilesystemFile

# JSON array of FilesystemFile.
FilesystemFileList = RootModel[list[FilesystemFile]]
