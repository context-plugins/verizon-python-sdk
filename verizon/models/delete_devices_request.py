from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict


class DeleteDevicesRequest(SdkBaseModel):
    """Request to delete a device request."""

    devices_to_delete: list[AccountDeviceList] = Field(alias="devicesToDelete")
    """A list of up to 100 devices that you want to delete, specified by device identifier. You only need to provide one
    identifier per device."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The Verizon billing account that the device group belongs to. An account name is usually numeric, and must
    include any leading zeros."""


class DeleteDevicesRequestDict(TypedDict):
    devices_to_delete: list[AccountDeviceList | AccountDeviceListDict]
    account_name: NotRequired[str]
