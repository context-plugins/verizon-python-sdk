from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GbiCarrierInformation5(SdkBaseModel):
    carrier_name: Optional[str] = Field(default=UNSET, alias="carrierName")


class GbiCarrierInformation5Dict(TypedDict):
    carrier_name: NotRequired[str]
