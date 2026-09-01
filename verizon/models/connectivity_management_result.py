from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectivityManagementResult(SdkBaseModel):
    """Response to errors."""

    error_code: Optional[str] = Field(default=UNSET, alias="errorCode")
    """Code of the error."""

    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """Details of the error."""


class ConnectivityManagementResultDict(TypedDict):
    error_code: NotRequired[str]
    error_message: NotRequired[str]
