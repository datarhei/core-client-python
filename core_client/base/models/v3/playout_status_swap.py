from pydantic import BaseModel


class PlayoutStatusSwap(BaseModel):
    """
    {
        "lasterror": "string",
        "lasturl": "string",
        "status": "string",
        "url": "string"
    }
    """

    lasterror: str | None = None
    lasturl: str | None = None
    status: str | None = None
    url: str | None = None
