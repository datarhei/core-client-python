from pydantic import RootModel
from typing import Union


Metadata = RootModel[Union[int, float, str, dict, list]]
