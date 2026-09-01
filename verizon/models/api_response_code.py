from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.response_code import ResponseCodeOrStr


class ApiResponseCode(SdkBaseModel):
    """ResponseCode and/or a message indicating success or failure of the request."""

    response_code: ResponseCodeOrStr = Field(alias="responseCode")
    """Possible response codes."""

    message: str
    """More details about the responseCode received."""


class ApiResponseCodeDict(TypedDict):
    response_code: ResponseCodeOrStr
    message: str
