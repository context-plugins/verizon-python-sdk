from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.device_ids import DeviceIds, DeviceIdsDict


class DeleteDevicesResult(SdkBaseModel):
    """Response for a request made to delete a device."""

    device_ids: Optional[DeviceIds] = Field(default=UNSET, alias="deviceIds")
    """One object per device to be deleted. Each object must contain a kind and id element identifying the device."""

    status: Optional[str] = UNSET
    """“Success” if the device was deleted, or “Failed” if there was a problem."""

    message: Optional[str] = UNSET
    """Not present if status=Success. One of these messages if status=Failed:The device is not in deactivate state.The
    user does not have access to delete the device."""


class DeleteDevicesResultDict(TypedDict):
    device_ids: NotRequired[DeviceIds | DeviceIdsDict]
    status: NotRequired[str]
    message: NotRequired[str]
