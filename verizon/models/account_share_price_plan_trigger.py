from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_share_filter_criteria import AccountShareFilterCriteria, AccountShareFilterCriteriaDict
from .change_plan_details import ChangePlanDetails, ChangePlanDetailsDict
from .unions.account_share_price_plan_trigger_condition import (
    AccountSharePricePlanTriggerCondition,
    AccountSharePricePlanTriggerConditionDict,
)


class AccountSharePricePlanTrigger(SdkBaseModel):
    account_share: Optional[AccountShareFilterCriteria] = Field(default=UNSET, alias="accountShare")
    condition: Optional[AccountSharePricePlanTriggerCondition] = UNSET
    change_plan: Optional[bool] = Field(default=UNSET, alias="changePlan")
    """a flag to set if the trigger changes service plans, true, or not, false"""

    change_plan_details: Optional[ChangePlanDetails] = Field(default=UNSET, alias="changePlanDetails")
    """The service plan code to switch to"""


class AccountSharePricePlanTriggerDict(TypedDict):
    account_share: NotRequired[AccountShareFilterCriteria | AccountShareFilterCriteriaDict]
    condition: NotRequired[AccountSharePricePlanTriggerCondition | AccountSharePricePlanTriggerConditionDict]
    change_plan: NotRequired[bool]
    change_plan_details: NotRequired[ChangePlanDetails | ChangePlanDetailsDict]
