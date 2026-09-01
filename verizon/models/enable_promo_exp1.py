from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EnablePromoExp1(SdkBaseModel):
    enable_promo_exp: Optional[bool] = Field(default=UNSET, alias="enablePromoExp")


class EnablePromoExp1Dict(TypedDict):
    enable_promo_exp: NotRequired[bool]
