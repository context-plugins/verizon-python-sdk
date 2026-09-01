from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_device_response import SearchDeviceResponse, SearchDeviceResponseDict


class SearchDeviceEventHistoryResponseList(SdkBaseModel):
    """A success response includes an array of all matching events."""

    search_device_event_history: Optional[list[SearchDeviceResponse]] = Field(
        default=UNSET, alias="SearchDeviceEventHistory"
    )


class SearchDeviceEventHistoryResponseListDict(TypedDict):
    search_device_event_history: NotRequired[list[SearchDeviceResponse | SearchDeviceResponseDict]]
