from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .find_device_by_property_response import FindDeviceByPropertyResponse, FindDeviceByPropertyResponseDict


class FindDeviceByPropertyResponseList(SdkBaseModel):
    """A success response includes an array of all matching devices. Each device includes the full device resource
    definition."""

    device_property: Optional[list[FindDeviceByPropertyResponse]] = Field(default=UNSET, alias="DeviceProperty")


class FindDeviceByPropertyResponseListDict(TypedDict):
    device_property: NotRequired[list[FindDeviceByPropertyResponse | FindDeviceByPropertyResponseDict]]
