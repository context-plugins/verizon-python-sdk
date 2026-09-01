from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .date_filter import DateFilter, DateFilterDict


class DeviceMismatchListRequest(SdkBaseModel):
    """Request to list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware)
    during a specified time frame."""

    filter: DateFilter
    """Filter out the dates."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """A list of specific devices that you want to check, specified by ICCID or MDN."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The account that you want to search for mismatched devices. If you don't specify an accountName, the search
    includes all devices to which you have access."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, to only include devices in that group."""


class DeviceMismatchListRequestDict(TypedDict):
    filter: DateFilter | DateFilterDict
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    account_name: NotRequired[str]
    group_name: NotRequired[str]
