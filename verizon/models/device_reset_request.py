from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict


class DeviceResetRequest(SdkBaseModel):
    """Request body to Performs a device reboot."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of the account. An account name is usually numeric, and must include any leading zeros."""

    action: Optional[str] = UNSET
    """The action you want to take on the device."""

    devices: Optional[list[Device]] = UNSET
    """The devices for which you want to perform a factory reset or reboot."""


class DeviceResetRequestDict(TypedDict):
    account_name: NotRequired[str]
    action: NotRequired[str]
    devices: NotRequired[list[Device | DeviceDict]]
