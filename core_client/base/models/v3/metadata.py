from pydantic import BaseModel
from typing import Union


class Metadata(BaseModel):
    __root__: Union[int, float, str, dict, list]
