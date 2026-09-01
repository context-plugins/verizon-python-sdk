from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FotaV2ResultError(SdkBaseModel):
    """Response for error cases."""

    error_code: str = Field(alias="errorCode")
    """Code of the error."""

    error_message: str = Field(alias="errorMessage")
    """Details of the error."""


class FotaV2ResultErrorDict(TypedDict):
    error_code: str
    error_message: str
