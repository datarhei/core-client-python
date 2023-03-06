from pydantic import BaseModel

from . import FilesystemOperationOrder


class FilesystemOperation(BaseModel):
    """
    {
        "from": "disk:/path/file",
        "operation": "copy",
        "to": "mem:/path/file"
    }
    from = source, to = target
    """

    source: str
    target: str
    operation: FilesystemOperationOrder
