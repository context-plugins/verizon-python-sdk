from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_group_share_object import AccountGroupShareObject, AccountGroupShareObjectDict
from .enums.active import ActiveOrStr
from .enums.trigger_category import TriggerCategoryOrStr
from .notificationarray import Notificationarray, NotificationarrayDict


class AccountGroupShareUpdateTriggerRequest(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """The system assigned UUID of the trigger"""

    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """The user defined name of the trigger"""

    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """The numeric name of the account and must include leading zeroes"""

    trigger_category: Optional[TriggerCategoryOrStr] = Field(default=UNSET, alias="triggerCategory")
    """The type of trigger being created or modified"""

    data_trigger: Optional[AccountGroupShareObject] = Field(default=UNSET, alias="dataTrigger")
    notification: Optional[Notificationarray] = UNSET
    active: Optional[ActiveOrStr] = UNSET
    """A flag to indicate of the trigger is active, true, or not, false"""


class AccountGroupShareUpdateTriggerRequestDict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    account_name: NotRequired[str]
    trigger_category: NotRequired[TriggerCategoryOrStr]
    data_trigger: NotRequired[AccountGroupShareObject | AccountGroupShareObjectDict]
    notification: NotRequired[Notificationarray | NotificationarrayDict]
    active: NotRequired[ActiveOrStr]
