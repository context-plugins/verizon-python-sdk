from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ReadySimServicePlan(SdkBaseModel):
    service_plan: Optional[str] = Field(default=UNSET, alias="servicePlan")


class ReadySimServicePlanDict(TypedDict):
    service_plan: NotRequired[str]
