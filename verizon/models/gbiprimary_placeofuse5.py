from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbi_address5 import GbiAddress5, GbiAddress5Dict
from .gbi_customer_name5 import GbiCustomerName5, GbiCustomerName5Dict


class GbiprimaryPlaceofuse5(SdkBaseModel):
    address: Optional[GbiAddress5] = UNSET
    customer_name: Optional[GbiCustomerName5] = Field(default=UNSET, alias="customerName")


class GbiprimaryPlaceofuse5Dict(TypedDict):
    address: NotRequired[GbiAddress5 | GbiAddress5Dict]
    customer_name: NotRequired[GbiCustomerName5 | GbiCustomerName5Dict]
