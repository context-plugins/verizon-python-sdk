from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ierror_message import IerrorMessage, IerrorMessageDict


class AggregateUsageError(SdkBaseModel):
    """Error reported by a device."""

    imei: Optional[str] = UNSET
    """The International Mobile Equipment Identifier of the device."""

    error_message: Optional[str] = Field(default=UNSET, alias="errorMessage")
    """A general error message."""

    error_response: Optional[IerrorMessage] = Field(default=UNSET, alias="errorResponse")
    """Error message."""


class AggregateUsageErrorDict(TypedDict):
    imei: NotRequired[str]
    error_message: NotRequired[str]
    error_response: NotRequired[IerrorMessage | IerrorMessageDict]
