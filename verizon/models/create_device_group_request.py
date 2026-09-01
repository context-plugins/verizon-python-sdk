from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class CreateDeviceGroupRequest(SdkBaseModel):
    """Create request for a new device group and optionally add devices to the group."""

    account_name: str = Field(alias="accountName")
    """The Verizon billing account that the device group will belong to. An account name is usually numeric, and must
    include any leading zeros."""

    group_description: str = Field(alias="groupDescription")
    """A description for the device group."""

    group_name: str = Field(alias="groupName")
    """The name for the new device group. This name must be unique within the specified account."""

    devices_to_add: Optional[list[DeviceId]] = Field(default=UNSET, alias="devicesToAdd")
    """Zero or more devices to add to the device group. You can use POST /devices/actions/list to get a list of all
    devices in the account."""


class CreateDeviceGroupRequestDict(TypedDict):
    account_name: str
    group_description: str
    group_name: str
    devices_to_add: NotRequired[list[DeviceId | DeviceIdDict]]
