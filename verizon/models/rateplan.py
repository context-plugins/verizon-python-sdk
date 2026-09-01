from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.rate_plan_group import RatePlanGroup, RatePlanGroupDict


class Rateplan(SdkBaseModel):
    rate_plan_group: Optional[list[RatePlanGroup]] = Field(default=UNSET, alias="ratePlanGroup")
    """An array of rate plan group names"""


class RateplanDict(TypedDict):
    rate_plan_group: NotRequired[list[RatePlanGroup | RatePlanGroupDict]]
