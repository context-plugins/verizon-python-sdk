from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .keyschunk2 import Keyschunk2, Keyschunk2Dict
from .ready_sim_service_plan import ReadySimServicePlan, ReadySimServicePlanDict


class PromoAlert(SdkBaseModel):
    filter_criteria: Optional[list[ReadySimServicePlan]] = Field(default=UNSET, alias="filterCriteria")
    condition: Optional[list[Keyschunk2]] = UNSET
    enable_promo_exp: Optional[bool] = Field(default=UNSET, alias="enablePromoExp")


class PromoAlertDict(TypedDict):
    filter_criteria: NotRequired[list[ReadySimServicePlan | ReadySimServicePlanDict]]
    condition: NotRequired[list[Keyschunk2 | Keyschunk2Dict]]
    enable_promo_exp: NotRequired[bool]
