from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict


class DeviceGroupDevicesData(SdkBaseModel):
    """Returns the name, description, and list of devices in a device group."""

    description: Optional[str] = UNSET
    """The description of the device group."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """The devices in the device group."""

    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    """False for a status 200 response.True for a status 202 response, indicating that there is more data to be
    retrieved."""

    name: Optional[str] = UNSET
    """The name of the device group."""


class DeviceGroupDevicesDataDict(TypedDict):
    description: NotRequired[str]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    has_more_data: NotRequired[bool]
    name: NotRequired[str]
