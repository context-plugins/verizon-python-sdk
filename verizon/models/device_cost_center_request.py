from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict


class DeviceCostCenterRequest(SdkBaseModel):
    """Request to retrieve cost center value of a device."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account."""

    cost_center: Optional[str] = Field(default=UNSET, alias="costCenter")
    """The new cost center code. Valid values are any string of up to 36 alphanumeric characters, space, dash,
    exclamation point, and pound sign."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """A list of the devices that you want to change, specified by device identifier. Do not include accountName,
    groupName, customFields, or servicePlan if you use this parameter."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to only include devices in that group."""

    primary_place_of_use: Optional[Any] = Field(default=UNSET, alias="primaryPlaceOfUse")
    """The customer name and the address of the device's primary place of use. These values are applied to all devices
    in the request.The Primary Place of Use location may affect taxation or have other legal implications. You may want
    to speak with legal and/or financial advisers before entering values for these fields."""

    remove_cost_center: Optional[bool] = Field(default=UNSET, alias="removeCostCenter")
    """Set to true to remove the cost center code value. This flag takes precedence over a new costCenter value. If this
    flag is true and costCenter has a value, the cost center code is removed. Do not include this parameter, or set it
    to false to change the costCenter value."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""


class DeviceCostCenterRequestDict(TypedDict):
    account_name: NotRequired[str]
    cost_center: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    group_name: NotRequired[str]
    primary_place_of_use: NotRequired[Any]
    remove_cost_center: NotRequired[bool]
    service_plan: NotRequired[str]
