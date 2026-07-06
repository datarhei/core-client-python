from pydantic import BaseModel


class ConfigCompress(BaseModel):
    """
    {
        "encoding": ["string"],
        "mimetypes": ["string"],
        "min_length": int
    }
    """

    encoding: list[str] | None = None
    mimetypes: list[str] | None = None
    min_length: int | None = None
