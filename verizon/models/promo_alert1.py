from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .keyschunk2 import Keyschunk2, Keyschunk2Dict


class PromoAlert1(SdkBaseModel):
    filter_criteria: Optional[list[Any]] = Field(default=UNSET, alias="filterCriteria")
    condition: Optional[list[Keyschunk2]] = UNSET
    enable_promo_exp: Optional[bool] = Field(default=UNSET, alias="enablePromoExp")


class PromoAlert1Dict(TypedDict):
    filter_criteria: NotRequired[list[Any]]
    condition: NotRequired[list[Keyschunk2 | Keyschunk2Dict]]
    enable_promo_exp: NotRequired[bool]
