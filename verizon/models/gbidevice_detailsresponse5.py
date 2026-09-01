from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbiaccount_nameobject5 import GbiaccountNameobject5, GbiaccountNameobject5Dict


class GbideviceDetailsresponse5(SdkBaseModel):
    has_more_data: Optional[bool] = Field(default=UNSET, alias="hasMoreData")
    devices: Optional[list[GbiaccountNameobject5]] = UNSET


class GbideviceDetailsresponse5Dict(TypedDict):
    has_more_data: NotRequired[bool]
    devices: NotRequired[list[GbiaccountNameobject5 | GbiaccountNameobject5Dict]]
