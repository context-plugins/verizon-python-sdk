from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsageTriggerUpdateRequest(SdkBaseModel):
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """Usage trigger name"""

    account_name: str = Field(alias="accountName")
    """Account name"""

    threshold_value: Optional[str] = Field(default=UNSET, alias="thresholdValue")
    """The percent of subscribed usage required to activate the trigger, such as 90 or 100."""

    sms_phone_numbers: Optional[str] = Field(default=UNSET, alias="smsPhoneNumbers")
    """Comma-separated list of phone numbers to send SMS alerts to. Digits only; no dashes or parentheses, etc."""

    email_addresses: Optional[str] = Field(default=UNSET, alias="emailAddresses")
    """Comma-separated list of email addresses to send alerts to."""


class UsageTriggerUpdateRequestDict(TypedDict):
    trigger_name: NotRequired[str]
    account_name: str
    threshold_value: NotRequired[str]
    sms_phone_numbers: NotRequired[str]
    email_addresses: NotRequired[str]
