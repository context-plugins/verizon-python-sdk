from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .data_trigger import DataTrigger, DataTriggerDict
from .enums.active import ActiveOrStr
from .enums.trigger_category import TriggerCategoryOrStr
from .notificationarray import Notificationarray, NotificationarrayDict
from .unions.sms_number_model import SmsNumberModel, SmsNumberModelDict


class AccountLevelCreateTriggerRequest(SdkBaseModel):
    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """The user defined name of the trigger"""

    ecpd_id: Optional[str] = Field(default=UNSET, alias="ecpdId")
    """The Enterprise Customer Profile Database ID"""

    trigger_category: Optional[TriggerCategoryOrStr] = Field(default=UNSET, alias="triggerCategory")
    """The type of trigger being created or modified"""

    data_trigger: Optional[DataTrigger] = Field(default=UNSET, alias="dataTrigger")
    notification: Optional[Notificationarray] = UNSET
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
    active: Optional[ActiveOrStr] = UNSET
    """A flag to indicate of the trigger is active, true, or not, false"""


class AccountLevelCreateTriggerRequestDict(TypedDict):
    trigger_name: NotRequired[str]
    ecpd_id: NotRequired[str]
    trigger_category: NotRequired[TriggerCategoryOrStr]
    data_trigger: NotRequired[DataTrigger | DataTriggerDict]
    notification: NotRequired[Notificationarray | NotificationarrayDict]
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
    active: NotRequired[ActiveOrStr]
