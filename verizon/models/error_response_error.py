from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorResponseError(SdkBaseModel):
    response_code: Optional[str] = Field(default=UNSET, alias="responseCode")
    message: Optional[str] = UNSET


class ErrorResponseErrorDict(TypedDict):
    response_code: NotRequired[str]
    message: NotRequired[str]
