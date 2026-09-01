from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CarrierServicePlan(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the service plan"""

    code: Optional[str] = UNSET
    """The inventory name or system name of the service plan"""

    size_kb: Optional[str] = Field(default=UNSET, alias="sizeKb")
    """The ammount of space the service plan will occupy on the Subscriber Information Module (SIM)"""

    carrier_service_plan_code: Optional[str] = Field(default=UNSET, alias="carrierServicePlanCode")
    """The billing record ID. This can be numeric, alpha or alphanumeric."""


class CarrierServicePlanDict(TypedDict):
    name: NotRequired[str]
    code: NotRequired[str]
    size_kb: NotRequired[str]
    carrier_service_plan_code: NotRequired[str]
