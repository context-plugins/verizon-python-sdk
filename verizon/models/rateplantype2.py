from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .accountid import Accountid, AccountidDict


class Rateplantype2(SdkBaseModel):
    description: Optional[str] = UNSET
    size_kb: Optional[str] = Field(default=UNSET, alias="sizeKb")
    carrier_rate_plan_code: Optional[str] = Field(default=UNSET, alias="carrierRatePlanCode")
    zero_dollar_billing: Optional[bool] = Field(default=UNSET, alias="zeroDollarBilling")
    promotion_offered: Optional[bool] = Field(default=UNSET, alias="promotionOffered")
    promotion_days: Optional[int] = Field(default=UNSET, alias="promotionDays")
    rate_plan_type: Optional[str] = Field(default=UNSET, alias="ratePlanType")
    account: Optional[list[Accountid]] = UNSET
    """Account information"""


class Rateplantype2Dict(TypedDict):
    description: NotRequired[str]
    size_kb: NotRequired[str]
    carrier_rate_plan_code: NotRequired[str]
    zero_dollar_billing: NotRequired[bool]
    promotion_offered: NotRequired[bool]
    promotion_days: NotRequired[int]
    rate_plan_type: NotRequired[str]
    account: NotRequired[list[Accountid | AccountidDict]]
