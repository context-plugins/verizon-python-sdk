from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_filter import DeviceFilter, DeviceFilterDict
from .enums.profile_status_filter import ProfileStatusFilterOrStr
from .enums.provisioning_status_filter import ProvisioningStatusFilterOrStr


class ESimglobalDeviceList(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account."""

    provisioning_status_filter: Optional[ProvisioningStatusFilterOrStr] = Field(
        default=UNSET, alias="provisioningStatusFilter"
    )
    """The last status of the device as a list filter."""

    profile_status_filter: Optional[ProfileStatusFilterOrStr] = Field(default=UNSET, alias="profileStatusFilter")
    """The last status of the device's profile as a filter."""

    carrier_name_filter: Optional[str] = Field(default=UNSET, alias="carrierNameFilter")
    """The cellular service provider."""

    device_filter: Optional[list[DeviceFilter]] = Field(default=UNSET, alias="deviceFilter")
    """An array of device identifiers to filter the list."""


class ESimglobalDeviceListDict(TypedDict):
    account_name: NotRequired[str]
    provisioning_status_filter: NotRequired[ProvisioningStatusFilterOrStr]
    profile_status_filter: NotRequired[ProfileStatusFilterOrStr]
    carrier_name_filter: NotRequired[str]
    device_filter: NotRequired[list[DeviceFilter | DeviceFilterDict]]
