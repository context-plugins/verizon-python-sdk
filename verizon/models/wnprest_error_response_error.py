from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WnprestErrorResponseError(SdkBaseModel):
    """Wireless network performance rest error response."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """Rest error response."""

    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """Error message details."""


class WnprestErrorResponseErrorDict(TypedDict):
    error_code: NotRequired[str]
    error_message: NotRequired[str]
