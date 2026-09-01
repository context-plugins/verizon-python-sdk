from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.sms_number_model import SmsNumberModel, SmsNumberModelDict


class Notificationarray(SdkBaseModel):
    notification_type: Optional[str] = Field(default=UNSET, alias="notificationType")
    callback: Optional[bool] = UNSET
    email_notification: Optional[bool] = Field(default=UNSET, alias="emailNotification")
    notification_group_name: Optional[str] = Field(default=UNSET, alias="notificationGroupName")
    notification_frequency_factor: Optional[int] = Field(default=UNSET, alias="notificationFrequencyFactor")
    notification_frequency_interval: Optional[str] = Field(default=UNSET, alias="notificationFrequencyInterval")
    external_email_recipients: Optional[str] = Field(default=UNSET, alias="externalEmailRecipients")
    sms_notification: Optional[bool] = Field(default=UNSET, alias="smsNotification")
    sms_numbers: Optional[list[SmsNumberModel]] = Field(default=UNSET, alias="smsNumbers")
    reminder: Optional[bool] = UNSET
    severity: Optional[str] = UNSET


class NotificationarrayDict(TypedDict):
    notification_type: NotRequired[str]
    callback: NotRequired[bool]
    email_notification: NotRequired[bool]
    notification_group_name: NotRequired[str]
    notification_frequency_factor: NotRequired[int]
    notification_frequency_interval: NotRequired[str]
    external_email_recipients: NotRequired[str]
    sms_notification: NotRequired[bool]
    sms_numbers: NotRequired[list[SmsNumberModel | SmsNumberModelDict]]
    reminder: NotRequired[bool]
    severity: NotRequired[str]
