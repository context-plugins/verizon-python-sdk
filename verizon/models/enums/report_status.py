from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReportStatus(str, Enum):
    """Status of the report."""

    QUEUED = "QUEUED"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"

    __str__ = str.__str__


ReportStatusOrStr: TypeAlias = Annotated[ReportStatus | str, open_enum_validator(ReportStatus)]
