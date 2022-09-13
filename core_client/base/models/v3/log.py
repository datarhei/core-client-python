from pydantic import BaseModel
from typing import List, Union


class Log(BaseModel):
    __root__: List[Union[str, dict]]
