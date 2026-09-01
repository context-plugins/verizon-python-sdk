from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.error_response_code import ErrorResponseCodeOrStr
from .enums.http_status_code import HttpStatusCodeOrStr


class IerrorMessage(SdkBaseModel):
    """Error message."""

    error_code: Optional[ErrorResponseCodeOrStr] = Field(default=UNSET, alias="errorCode")
    """Error Code."""

    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """Details and additional information about the error code."""

    http_status_code: Optional[HttpStatusCodeOrStr] = Field(default=UNSET, alias="httpStatusCode")
    """HTML error code and description."""

    detail_error_message: Optional[str] = Field(default=UNSET, alias="detailErrorMessage")
    """More detail and information about the HTML error code."""


class IerrorMessageDict(TypedDict):
    error_code: NotRequired[ErrorResponseCodeOrStr]
    error_message: NotRequired[str]
    http_status_code: NotRequired[HttpStatusCodeOrStr]
    detail_error_message: NotRequired[str]
