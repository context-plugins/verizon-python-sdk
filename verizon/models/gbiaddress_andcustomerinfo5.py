from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbiprimary_placeofuse5 import GbiprimaryPlaceofuse5, GbiprimaryPlaceofuse5Dict


class GbiaddressAndcustomerinfo5(SdkBaseModel):
    primary_placeofuse: Optional[GbiprimaryPlaceofuse5] = Field(default=UNSET, alias="primaryPlaceofuse")


class GbiaddressAndcustomerinfo5Dict(TypedDict):
    primary_placeofuse: NotRequired[GbiprimaryPlaceofuse5 | GbiprimaryPlaceofuse5Dict]
