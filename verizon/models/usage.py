from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_fields import CustomFields, CustomFieldsDict


class Usage(SdkBaseModel):
    """The daily network data usage of a single device during a specified time period."""

    bytes_used: Optional[int] = Field(default=UNSET, alias="bytesUsed")
    """The number of bytes that the device sent or received on the report date."""

    extended_attributes: Optional[list[CustomFields]] = Field(default=UNSET, alias="extendedAttributes")
    """The number of mobile-originated and mobile-terminated SMS messages on the report date."""

    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")
    """The list of service plans associated with the device/account."""

    sms_used: Optional[int] = Field(default=UNSET, alias="smsUsed")
    """The number of SMS messages that were sent or received on the report date."""

    source: Optional[str] = UNSET
    """The source of the information for the reported usage."""

    timestamp: Optional[str] = UNSET
    """The date of the recorded usage."""


class UsageDict(TypedDict):
    bytes_used: NotRequired[int]
    extended_attributes: NotRequired[list[CustomFields | CustomFieldsDict]]
    service_plan: NotRequired[str]
    sms_used: NotRequired[int]
    source: NotRequired[str]
    timestamp: NotRequired[str]
