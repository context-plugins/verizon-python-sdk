from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .actionobject import Actionobject, ActionobjectDict
from .pay_as_you_go_filter_criteria import PayAsYouGoFilterCriteria, PayAsYouGoFilterCriteriaDict
from .unions.pay_as_you_go_price_plan_trigger_condition import (
    PayAsYouGoPricePlanTriggerCondition,
    PayAsYouGoPricePlanTriggerConditionDict,
)


class PayAsYouGoPricePlanTrigger(SdkBaseModel):
    pay_as_you_go: Optional[PayAsYouGoFilterCriteria] = Field(default=UNSET, alias="payAsYouGo")
    condition: Optional[PayAsYouGoPricePlanTriggerCondition] = UNSET
    action: Optional[Actionobject] = UNSET


class PayAsYouGoPricePlanTriggerDict(TypedDict):
    pay_as_you_go: NotRequired[PayAsYouGoFilterCriteria | PayAsYouGoFilterCriteriaDict]
    condition: NotRequired[PayAsYouGoPricePlanTriggerCondition | PayAsYouGoPricePlanTriggerConditionDict]
    action: NotRequired[Actionobject | ActionobjectDict]
