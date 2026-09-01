from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict
from .device_id import DeviceId, DeviceIdDict


class SmssendRequest(SdkBaseModel):
    """Request to send SMS."""

    account_name: str = Field(alias="accountName")
    """The name of a billing account."""

    sms_message: str = Field(alias="smsMessage")
    """The contents of the SMS message. The SMS message is limited to 160 characters in 7-bit format, or 140 characters
    in 8-bit format."""

    custom_fields: Optional[list[CustomFields]] = Field(default=UNSET, alias="customFields")
    """The names and values of custom fields, if you want to only include devices that have matching custom fields."""

    data_encoding: Optional[str] = Field(default=UNSET, alias="dataEncoding")
    """The SMS message encoding, which can be 7-bit (default), 8-bit-ASCII, 8-bit-UTF-8, 8-bit-DATA."""

    device_ids: Optional[list[DeviceId]] = Field(default=UNSET, alias="deviceIds")
    """The devices that you want to send the message to, specified by device identifier."""

    group_name: Optional[str] = Field(default=UNSET, alias="groupName")
    """The name of a device group, if you want to send the SMS message to all devices in the device group."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The name of a service plan, if you want to only include devices that have that service plan."""

    time_to_live: Optional[str] = Field(default=UNSET, alias="timeToLive")
    """A period of time the message remains valid or an end date for the message. This value would be less than the 5
    day default."""


class SmssendRequestDict(TypedDict):
    account_name: str
    sms_message: str
    custom_fields: NotRequired[list[CustomFields | CustomFieldsDict]]
    data_encoding: NotRequired[str]
    device_ids: NotRequired[list[DeviceId | DeviceIdDict]]
    group_name: NotRequired[str]
    service_plan: NotRequired[str]
    time_to_live: NotRequired[str]
