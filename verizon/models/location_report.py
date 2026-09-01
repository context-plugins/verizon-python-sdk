from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .location import Location, LocationDict


class LocationReport(SdkBaseModel):
    """Location information for up to 1,000 devices."""

    dev_location_list: Optional[list[Location]] = Field(default=UNSET, alias="devLocationList")
    """Device location information."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """True if there are more device locations to retrieve."""

    start_index: Optional[str] = Field(default=UNSET, alias="startIndex")
    """The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more
    than 1,000 devices to be returned (hasMoreData=true), set startIndex=1000 for the second request, 2000 for the third
    request, etc."""

    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")
    """The total number of devices in the original request and in the report."""

    txid: Optional[str] = UNSET
    """The transaction ID of the report."""


class LocationReportDict(TypedDict):
    dev_location_list: NotRequired[list[Location | LocationDict]]
    has_more_data: NotRequired[bool]
    start_index: NotRequired[str]
    total_count: NotRequired[int]
    txid: NotRequired[str]
