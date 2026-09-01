from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ChangePlanDetails(SdkBaseModel):
    """The service plan code to switch to"""

    to_carrier_service_plan_code: Optional[str] = Field(default=UNSET, alias="toCarrierServicePlanCode")


class ChangePlanDetailsDict(TypedDict):
    to_carrier_service_plan_code: NotRequired[str]
