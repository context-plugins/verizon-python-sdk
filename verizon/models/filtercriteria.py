from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ready_sim_service_plan import ReadySimServicePlan, ReadySimServicePlanDict


class Filtercriteria(SdkBaseModel):
    filter_criteria: Optional[list[ReadySimServicePlan]] = Field(default=UNSET, alias="filterCriteria")


class FiltercriteriaDict(TypedDict):
    filter_criteria: NotRequired[list[ReadySimServicePlan | ReadySimServicePlanDict]]
