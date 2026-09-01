from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.service_name import ServiceNameOrStr


class UsageTriggerResponse(SdkBaseModel):
    trigger_id: str = Field(alias="triggerId")
    """Unique usage triggerId"""

    trigger_name: str = Field(alias="triggerName")
    """Usage trigger name"""

    account_name: str = Field(alias="accountName")
    """Account name"""

    service_name: ServiceNameOrStr = Field(alias="serviceName")
    """Service name"""

    threshold_value: str = Field(alias="thresholdValue")
    """Percent of subscription at which trigger will send an alert"""

    allow_excess: bool = Field(alias="allowExcess")
    """allowExcess determines whether to restrict usage after exceeds limits"""

    send_sms_notification: bool = Field(alias="sendSmsNotification")
    """Send SMS (text) alerts when the thresholdValue is reached."""

    sms_phone_numbers: str = Field(alias="smsPhoneNumbers")
    """comma seperated value of list of Phone numbers for SMS notifications"""

    send_email_notification: bool = Field(alias="sendEmailNotification")
    """Send email alerts when the thresholdValue is reached."""

    email_addresses: str = Field(alias="emailAddresses")
    """comma seperated value of list of Email addresses for Email notifications"""

    create_date: str = Field(alias="createDate")
    """UTC Date when the usage trigger was created"""

    update_date: str = Field(alias="updateDate")
    """UTC Date when the usage trigger was last updated"""


class UsageTriggerResponseDict(TypedDict):
    trigger_id: str
    trigger_name: str
    account_name: str
    service_name: ServiceNameOrStr
    threshold_value: str
    allow_excess: bool
    send_sms_notification: bool
    sms_phone_numbers: str
    send_email_notification: bool
    email_addresses: str
    create_date: str
    update_date: str
