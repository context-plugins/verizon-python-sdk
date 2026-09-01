from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .change_plan_details import ChangePlanDetails, ChangePlanDetailsDict
from .suspenddetailsobject import Suspenddetailsobject, SuspenddetailsobjectDict


class Actionobject(SdkBaseModel):
    suspend: Optional[bool] = UNSET
    suspend_details: Optional[Suspenddetailsobject] = Field(default=UNSET, alias="suspendDetails")
    change_plan: Optional[bool] = Field(default=UNSET, alias="changePlan")
    """a flag to set if the trigger changes service plans, true, or not, false"""

    change_plan_details: Optional[ChangePlanDetails] = Field(default=UNSET, alias="changePlanDetails")
    """The service plan code to switch to"""


class ActionobjectDict(TypedDict):
    suspend: NotRequired[bool]
    suspend_details: NotRequired[Suspenddetailsobject | SuspenddetailsobjectDict]
    change_plan: NotRequired[bool]
    change_plan_details: NotRequired[ChangePlanDetails | ChangePlanDetailsDict]
