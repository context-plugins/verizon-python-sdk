from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AggregatedReportCallbackStatus(str, Enum):
    """QUEUED or COMPLETED. Requests for IoT devices with cacheMode=0 (cached) have status=COMPLETED; all other requests
    are QUEUED."""

    QUEUED = "QUEUED"
    COMPLETED = "COMPLETED"

    __str__ = str.__str__


AggregatedReportCallbackStatusOrStr: TypeAlias = Annotated[
    AggregatedReportCallbackStatus | str, open_enum_validator(AggregatedReportCallbackStatus)
]
