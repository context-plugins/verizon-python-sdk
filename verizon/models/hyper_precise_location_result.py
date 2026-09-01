from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error_response_code import ErrorResponseCodeOrStr
from .hyper_precise_location_fault import HyperPreciseLocationFault, HyperPreciseLocationFaultDict


class HyperPreciseLocationResult(SdkBaseModel):
    """Error response."""

    response_code: Optional[ErrorResponseCodeOrStr] = Field(default=UNSET, alias="responseCode")
    """Error Code."""

    message: Optional[str] = UNSET
    """Error message."""

    fault: Optional[HyperPreciseLocationFault] = UNSET
    """Fault occurred while responding."""


class HyperPreciseLocationResultDict(TypedDict):
    response_code: NotRequired[ErrorResponseCodeOrStr]
    message: NotRequired[str]
    fault: NotRequired[HyperPreciseLocationFault | HyperPreciseLocationFaultDict]
