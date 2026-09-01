from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class DeviceGroupUpdateRequest(SdkBaseModel):
    """Make changes to a device group, including changing the name and description, and adding or removing devices."""

    devices_to_add: Optional[list[DeviceId]] = Field(default=UNSET, alias="devicesToAdd")
    """Zero or more devices to add to the device group, specified by device ID. The devices will be removed from their
    current device groups. You can use POST /devices/actions/list to get a list of all devices in the account."""

    devices_to_remove: Optional[list[DeviceId]] = Field(default=UNSET, alias="devicesToRemove")
    """Zero or more devices to remove from the device group, specified by device ID. The devices will be added to the
    default device group."""

    new_group_description: Optional[str] = Field(default=UNSET, alias="newGroupDescription")
    """A new description for the device group. Do not include this parameter to leave the group description
    unchanged."""

    new_group_name: Optional[str] = Field(default=UNSET, alias="newGroupName")
    """A new name for the device group. Do not include this parameter if you want to leave the group name unchanged."""


class DeviceGroupUpdateRequestDict(TypedDict):
    devices_to_add: NotRequired[list[DeviceId | DeviceIdDict]]
    devices_to_remove: NotRequired[list[DeviceId | DeviceIdDict]]
    new_group_description: NotRequired[str]
    new_group_name: NotRequired[str]
