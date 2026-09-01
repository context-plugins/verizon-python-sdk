from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbiaddress_andcustomerinfo5 import GbiaddressAndcustomerinfo5, GbiaddressAndcustomerinfo5Dict


class GbiaddressAndcustomerinfo25(SdkBaseModel):
    primary_placeofuse: Optional[GbiaddressAndcustomerinfo5] = Field(default=UNSET, alias="primaryPlaceofuse")


class GbiaddressAndcustomerinfo25Dict(TypedDict):
    primary_placeofuse: NotRequired[GbiaddressAndcustomerinfo5 | GbiaddressAndcustomerinfo5Dict]
