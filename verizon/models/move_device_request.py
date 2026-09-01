from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict
from .device_filter import DeviceFilter, DeviceFilterDict


class MoveDeviceRequest(SdkBaseModel):
    """Request to move active devices from one billing account to another within a customer profile."""

    account_name: str = Field(alias="accountName")
    """The name of the billing account that you want to move the devices to."""

    filter: Optional[DeviceFilter] = UNSET
    """Specify the kind of the device identifier, the type of match, and the string that you want to match."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """Up to 10,000 devices that you want to move to a different account, specified by device identifier."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, to only include devices in that group."""

    carrier_ip_pool_name: Optional[str] = Field(default=UNSET, alias="carrierIpPoolName")
    """The pool from which device IP addresses will be derived in the new account. If you do not include this element,
    the default pool will be used."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The service plan code that you want to assign to the devices in the new account. If you do not include this
    element, ThingSpace will attempt to use the current service plan, which will result in a error if the new account
    does not have that service plan."""


class MoveDeviceRequestDict(TypedDict):
    account_name: str
    filter: NotRequired[DeviceFilter | DeviceFilterDict]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    group_name: NotRequired[str]
    carrier_ip_pool_name: NotRequired[str]
    service_plan: NotRequired[str]
