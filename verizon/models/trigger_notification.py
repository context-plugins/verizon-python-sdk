from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .smsnumber import Smsnumber, SmsnumberDict


class TriggerNotification(SdkBaseModel):
    """The notification details of the trigger."""

    notification_type: Optional[str] = Field(default=UNSET, alias="notificationType")
    """The type of notification, i.e. 'DailySummary'."""

    callback: Optional[bool] = UNSET
    """Whether or not the notification should be sent via callback.<br />true<br />false."""

    email_notification: Optional[bool] = Field(default=UNSET, alias="emailNotification")
    """Whether or not the notification should be sent via e-mail.<br />true<br />false."""

    notification_group_name: Optional[str] = Field(default=UNSET, alias="notificationGroupName")
    """Name for the notification group."""

    notification_frequency_factor: Optional[int] = Field(default=UNSET, alias="notificationFrequencyFactor")
    """Frequency factor for notification."""

    notification_frequency_interval: Optional[str] = Field(default=UNSET, alias="notificationFrequencyInterval")
    """Frequency interval for notification."""

    external_email_recipients: Optional[str] = Field(default=UNSET, alias="externalEmailRecipients")
    """E-mail address(es) where the notification should be delivered."""

    sms_notification: Optional[bool] = Field(default=UNSET, alias="smsNotification")
    """SMS notification."""

    sms_numbers: Optional[list[Smsnumber]] = Field(default=UNSET, alias="smsNumbers")
    """List of SMS numbers."""

    reminder: Optional[bool] = UNSET
    severity: Optional[str] = UNSET
    """Severity level associated with the notification. Examples would be:<br />Major<br />Minor<br />Critical<br
    />NotApplicable."""


class TriggerNotificationDict(TypedDict):
    notification_type: NotRequired[str]
    callback: NotRequired[bool]
    email_notification: NotRequired[bool]
    notification_group_name: NotRequired[str]
    notification_frequency_factor: NotRequired[int]
    notification_frequency_interval: NotRequired[str]
    external_email_recipients: NotRequired[str]
    sms_notification: NotRequired[bool]
    sms_numbers: NotRequired[list[Smsnumber | SmsnumberDict]]
    reminder: NotRequired[bool]
    severity: NotRequired[str]
