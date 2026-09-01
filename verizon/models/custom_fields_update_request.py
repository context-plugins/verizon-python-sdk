from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_device_list import AccountDeviceList, AccountDeviceListDict
from .custom_fields import CustomFields, CustomFieldsDict


class CustomFieldsUpdateRequest(SdkBaseModel):
    """Request to assign or change custom field values for one or more devices."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account.This parameter is only required if the UWS account used for the current API session
    has access to multiple billing accounts.An account name is usually numeric, and must include any leading zeros."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """Custom field names and values, if you want to only include devices that have matching values."""

    custom_fields_to_update: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFieldsToUpdate")
    """The names and new values of any custom fields that you want to change."""

    devices: Optional[list[AccountDeviceList]] = UNSET
    """The devices that you want to change."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to only include devices in that group."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""


class CustomFieldsUpdateRequestDict(TypedDict):
    account_name: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    custom_fields_to_update: NotRequired[list[CustomFields | CustomFieldsDict]]
    devices: NotRequired[list[AccountDeviceList | AccountDeviceListDict]]
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
