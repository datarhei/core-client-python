from pydantic import RootModel

from . import Process

# JSON array of Process.
ProcessList = RootModel[list[Process]]
