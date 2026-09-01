from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list_filter import AccountDeviceListFilter, AccountDeviceListFilterDict
from .custom_fields import CustomFields, CustomFieldsDict
from .device_id import DeviceId, DeviceIdDict


class AccountDeviceListRequest(SdkBaseModel):
    """Request for listing account devices."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The billing account for which a list of devices is returned. If you don't specify an accountName, the list
    includes all devices to which you have access."""

    device_id: Optional[DeviceId] = Field(default=UNSET, alias="deviceId")
    """An identifier for a single device."""

    filter: Optional[AccountDeviceListFilter] = UNSET
    """Filter for a list of devices."""

    current_state: Optional[str] = Field(default=UNSET, alias="currentState")
    """The name of a device state, to only include devices in that state."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    earliest: Optional[str] = UNSET
    """Only include devices that were added after this date and time."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """Only include devices that are in this device group."""

    latest: Optional[str] = UNSET
    """Only include devices that were added before this date and time."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """Only include devices that have this service plan."""

    max_number_of_devices: Optional[int] = Field(default=UNSET, alias="maxNumberOfDevices")
    largest_device_id_seen: Optional[int] = Field(default=UNSET, alias="largestDeviceIdSeen")


class AccountDeviceListRequestDict(TypedDict):
    account_name: NotRequired[str]
    device_id: NotRequired[DeviceId | DeviceIdDict]
    filter: NotRequired[AccountDeviceListFilter | AccountDeviceListFilterDict]
    current_state: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    earliest: NotRequired[str]
    group_name: NotRequired[str]
    latest: NotRequired[str]
    service_plan: NotRequired[str]
    max_number_of_devices: NotRequired[int]
    largest_device_id_seen: NotRequired[int]
