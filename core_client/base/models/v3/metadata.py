from pydantic import BaseModel, RootModel
from typing import Union


class Metadata(BaseModel):
    RootModel: Union[int, float, str, dict, list]
