from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FotaV3Result(SdkBaseModel):
    """Error response."""

    error_code: str = Field(alias="errorCode")
    """Error code string."""

    error_message: str = Field(alias="errorMessage")
    """Error message string."""


class FotaV3ResultDict(TypedDict):
    error_code: str
    error_message: str
