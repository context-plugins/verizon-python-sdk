from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_filter_without_account import DeviceFilterWithoutAccount, DeviceFilterWithoutAccountDict
from .device_id import DeviceId, DeviceIdDict


class DeviceSuspensionStatusRequest(SdkBaseModel):
    """Request to return service suspension information about one or more devices."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """The devices that you want to include in the request, specified by device identifier. You only need to provide one
    identifier per device."""

    filter: Optional[DeviceFilterWithoutAccount] = UNSET
    """Filter for devices without account."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""


class DeviceSuspensionStatusRequestDict(TypedDict):
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    filter: NotRequired[DeviceFilterWithoutAccount | DeviceFilterWithoutAccountDict]
    account_name: NotRequired[str]
