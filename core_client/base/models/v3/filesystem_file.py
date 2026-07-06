from pydantic import BaseModel


class FilesystemFile(BaseModel):
    name: str
    size_bytes: int
    last_modified: int
    core_id: str | None = None
