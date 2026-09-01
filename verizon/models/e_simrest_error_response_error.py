from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ESimrestErrorResponseError(SdkBaseModel):
    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")


class ESimrestErrorResponseErrorDict(TypedDict):
    error_code: NotRequired[str]
    error_message: NotRequired[str]
