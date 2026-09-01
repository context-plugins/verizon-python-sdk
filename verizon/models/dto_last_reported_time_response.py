from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .resource_event import ResourceEvent, ResourceEventDict


class DtoLastReportedTimeResponse(SdkBaseModel):
    event: Optional[ResourceEvent] = UNSET
    timestamp: Optional[str] = UNSET


class DtoLastReportedTimeResponseDict(TypedDict):
    event: NotRequired[ResourceEvent | ResourceEventDict]
    timestamp: NotRequired[str]
