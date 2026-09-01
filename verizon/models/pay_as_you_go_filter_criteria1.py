from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PayAsYouGoFilterCriteria1(SdkBaseModel):
    carrier_service_plan_code: Optional[str] = Field(default=UNSET, alias="carrierServicePlanCode")
    account_name_list: Optional[list[str]] = Field(default=UNSET, alias="accountNameList")
    """An array of account names"""


class PayAsYouGoFilterCriteria1Dict(TypedDict):
    carrier_service_plan_code: NotRequired[str]
    account_name_list: NotRequired[list[str]]
