from pydantic import RootModel

from . import ReportProcess

# JSON array of ReportProcess.
ReportProcessList = RootModel[list[ReportProcess]]
