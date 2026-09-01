from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_share_price_plan_trigger import AccountSharePricePlanTrigger, AccountSharePricePlanTriggerDict
from .enums.active import ActiveOrStr
from .enums.trigger_category import TriggerCategoryOrStr
from .notificationarray import Notificationarray, NotificationarrayDict


class AccountShareUpdateTriggerRequest(SdkBaseModel):
    trigger_id: Optional[str] = Field(default=UNSET, alias="triggerId")
    """The system assigned UUID of the trigger"""

    trigger_name: Optional[str] = Field(default=UNSET, alias="triggerName")
    """The user defined name of the trigger"""

    ecpd_id: Optional[str] = Field(default=UNSET, alias="ecpdId")
    """The Enterprise Customer Profile Database ID"""

    trigger_category: Optional[TriggerCategoryOrStr] = Field(default=UNSET, alias="triggerCategory")
    """The type of trigger being created or modified"""

    price_plan_trigger: Optional[AccountSharePricePlanTrigger] = Field(default=UNSET, alias="pricePlanTrigger")
    notification: Optional[Notificationarray] = UNSET
    active: Optional[ActiveOrStr] = UNSET
    """A flag to indicate of the trigger is active, true, or not, false"""


class AccountShareUpdateTriggerRequestDict(TypedDict):
    trigger_id: NotRequired[str]
    trigger_name: NotRequired[str]
    ecpd_id: NotRequired[str]
    trigger_category: NotRequired[TriggerCategoryOrStr]
    price_plan_trigger: NotRequired[AccountSharePricePlanTrigger | AccountSharePricePlanTriggerDict]
    notification: NotRequired[Notificationarray | NotificationarrayDict]
    active: NotRequired[ActiveOrStr]
