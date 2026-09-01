from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_device_by_property_response import SearchDeviceByPropertyResponse, SearchDeviceByPropertyResponseDict


class SearchDeviceByPropertyResponseList(SdkBaseModel):
    """A success response includes an array of all matching devices."""

    device_property: Optional[list[SearchDeviceByPropertyResponse]] = Field(default=UNSET, alias="DeviceProperty")


class SearchDeviceByPropertyResponseListDict(TypedDict):
    device_property: NotRequired[list[SearchDeviceByPropertyResponse | SearchDeviceByPropertyResponseDict]]
