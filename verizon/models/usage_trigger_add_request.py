from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.service_name import ServiceNameOrStr


class UsageTriggerAddRequest(SdkBaseModel):
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """Usage trigger name"""

    account_name: str = Field(alias="accountName")
    """Account name"""

    service_name: ServiceNameOrStr = Field(alias="serviceName")
    """Service name"""

    threshold_value: str = Field(alias="thresholdValue")
    """The percent of subscribed usage required to activate the trigger, such as 90 or 100."""

    allow_excess: Optional[bool] = Field(default=UNSET, alias="allowExcess")
    """Allow additional requests after thresholdValue is reached. (currently not functional)"""

    send_sms_notification: Optional[bool] = Field(default=UNSET, alias="sendSmsNotification")
    """Send SMS (text) alerts when the thresholdValue is reached."""

    sms_phone_numbers: Optional[str] = Field(default=UNSET, alias="smsPhoneNumbers")
    """Comma-separated list of phone numbers to send SMS alerts to. Digits only; no dashes or parentheses, etc."""

    send_email_notification: Optional[bool] = Field(default=UNSET, alias="sendEmailNotification")
    """Send email alerts when the thresholdValue is reached."""

    email_addresses: Optional[str] = Field(default=UNSET, alias="emailAddresses")
    """Comma-separated list of email addresses to send alerts to."""


class UsageTriggerAddRequestDict(TypedDict):
    trigger_name: NotRequired[str]
    account_name: str
    service_name: ServiceNameOrStr
    threshold_value: str
    allow_excess: NotRequired[bool]
    send_sms_notification: NotRequired[bool]
    sms_phone_numbers: NotRequired[str]
    send_email_notification: NotRequired[bool]
    email_addresses: NotRequired[str]
