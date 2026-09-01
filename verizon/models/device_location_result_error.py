from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceLocationResultError(SdkBaseModel):
    """Will be empty if there was no error."""

    error_code: str = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")


class DeviceLocationResultErrorDict(TypedDict):
    error_code: str
    error_message: str
