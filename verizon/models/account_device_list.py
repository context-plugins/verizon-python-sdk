from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class AccountDeviceList(SdkBaseModel):
    """A list of deviceId objects to use when requesting information from multiple devices."""

    device_ids: list[DeviceId] = Field(alias="deviceIds")
    """All identifiers for the device."""

    ip_address: Optional[str] = Field(default=UNSET, alias="ipAddress")


class AccountDeviceListDict(TypedDict):
    device_ids: list[DeviceId | DeviceIdDict]
    ip_address: NotRequired[str]
