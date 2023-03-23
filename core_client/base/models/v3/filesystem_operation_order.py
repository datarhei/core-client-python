from enum import Enum


class FilesystemOperationOrder(str, Enum):
    """
    "operation": "copy"
    """

    copy = "copy"
    move = "move"

    class Config:
        use_enum_values = True
