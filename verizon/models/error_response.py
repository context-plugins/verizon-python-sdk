from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorResponse(SdkBaseModel):
    response_code: Optional[str] = Field(default=UNSET, alias="responseCode")
    message: Optional[str] = UNSET


class ErrorResponseDict(TypedDict):
    response_code: NotRequired[str]
    message: NotRequired[str]
