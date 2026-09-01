from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FotaV1Result(SdkBaseModel):
    """Response in case of any errors."""

    error_code: str = Field(alias="errorCode")
    """Error response code."""

    error_message: str = Field(alias="errorMessage")
    """Description of the error."""


class FotaV1ResultDict(TypedDict):
    error_code: str
    error_message: str
