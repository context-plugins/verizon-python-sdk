from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rateplantype2 import Rateplantype2, Rateplantype2Dict


class RateplantypeObject(SdkBaseModel):
    rate_plan_group_description: Optional[str] = Field(default=UNSET, alias="ratePlanGroupDescription")
    rate_plan_type: Optional[str] = Field(default=UNSET, alias="ratePlanType")
    rate_plan: Optional[list[Rateplantype2]] = Field(default=UNSET, alias="ratePlan")
    """An array of rateplan names"""


class RateplantypeObjectDict(TypedDict):
    rate_plan_group_description: NotRequired[str]
    rate_plan_type: NotRequired[str]
    rate_plan: NotRequired[list[Rateplantype2 | Rateplantype2Dict]]
