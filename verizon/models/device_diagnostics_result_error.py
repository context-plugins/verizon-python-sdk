from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceDiagnosticsResultError(SdkBaseModel):
    """All error messages are returned in this format. Error codes and messages are listed on the Error Codes page,
    along with explanations and suggestions for corrective actions."""

    error_code: str = Field(alias="errorCode")
    """Simple error code."""

    error_message: str = Field(alias="errorMessage")
    """Detailed error message."""


class DeviceDiagnosticsResultErrorDict(TypedDict):
    error_code: str
    error_message: str
