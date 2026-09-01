from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict
from .device_id import DeviceId, DeviceIdDict


class DevicePrlListRequest(SdkBaseModel):
    """Requests the current PRL (Preferred Roaming List) version for 2G or 3G devices, which can help determine which
    devices need a PRL update. (4G and GSM devices do not have a PRL.)."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """The devices for which you want the PRL version, specified by device identifier. You only need to provide one
    identifier per device. Do not use any of the other parameters if you specify device IDs."""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The name of a billing account. This parameter is only required if you are passing groupName and the UWS account
    used for the current API session has access to multiple billing accounts, because the same device group name can
    exist in multiple accounts.An account name is usually numeric, and must include any leading zeros."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """The names and values of custom fields, if you want to only include devices that have matching custom fields."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to only include devices in that group."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""


class DevicePrlListRequestDict(TypedDict):
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    account_name: NotRequired[str]
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
