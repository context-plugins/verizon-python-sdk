from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .actionobject import Actionobject, ActionobjectDict
from .filtercriteria_object_call import FiltercriteriaObjectCall, FiltercriteriaObjectCallDict
from .unions.price_plan_trigger_condition import PricePlanTriggerCondition, PricePlanTriggerConditionDict


class PricePlanTrigger(SdkBaseModel):
    stand_alone: Optional[FiltercriteriaObjectCall] = Field(default=UNSET, alias="standAlone")
    condition: Optional[PricePlanTriggerCondition] = UNSET
    action: Optional[Actionobject] = UNSET


class PricePlanTriggerDict(TypedDict):
    stand_alone: NotRequired[FiltercriteriaObjectCall | FiltercriteriaObjectCallDict]
    condition: NotRequired[PricePlanTriggerCondition | PricePlanTriggerConditionDict]
    action: NotRequired[Actionobject | ActionobjectDict]
