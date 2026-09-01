from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class AddDevicesResult(SdkBaseModel):
    """Contains the device identifiers and a success or failure response for each device in the request."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """Identifiers for the device."""

    response: Optional[str] = UNSET
    """The status message for the current device. This will be Success or Failed"""


class AddDevicesResultDict(TypedDict):
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    response: NotRequired[str]
