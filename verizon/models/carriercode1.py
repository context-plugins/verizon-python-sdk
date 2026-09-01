from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .allowance_threshold import AllowanceThreshold, AllowanceThresholdDict


class Carriercode1(SdkBaseModel):
    carrier_code: Optional[str] = Field(default=UNSET, alias="carrierCode")
    percentage: Optional[AllowanceThreshold] = UNSET


class Carriercode1Dict(TypedDict):
    carrier_code: NotRequired[str]
    percentage: NotRequired[AllowanceThreshold | AllowanceThresholdDict]
