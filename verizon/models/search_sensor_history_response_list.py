from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_device_response import SearchDeviceResponse, SearchDeviceResponseDict


class SearchSensorHistoryResponseList(SdkBaseModel):
    """A success response includes an array of all matching events."""

    search_sensor_history: Optional[list[SearchDeviceResponse]] = Field(default=UNSET, alias="SearchSensorHistory")


class SearchSensorHistoryResponseListDict(TypedDict):
    search_sensor_history: NotRequired[list[SearchDeviceResponse | SearchDeviceResponseDict]]
