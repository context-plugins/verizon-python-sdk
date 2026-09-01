from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IntelligenceResultError(SdkBaseModel):
    """An error occurred."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """The 3-digit HTML error code."""

    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """Error Message."""


class IntelligenceResultErrorDict(TypedDict):
    error_code: NotRequired[str]
    error_message: NotRequired[str]
