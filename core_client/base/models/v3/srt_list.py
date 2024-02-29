from pydantic import RootModel
from typing import List

from . import Srt


SrtList = RootModel[List[Srt]]