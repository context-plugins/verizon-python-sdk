from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PositionError(SdkBaseModel):
    """Position error."""

    time: Optional[str] = UNSET
    """Time location obtained."""

    utcoffset: Optional[str] = UNSET
    """UTC offset of time."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Error type returned from location server."""

    info: Optional[str] = UNSET
    """Additional information about the error."""


class PositionErrorDict(TypedDict):
    time: NotRequired[str]
    utcoffset: NotRequired[str]
    type_: NotRequired[str]
    info: NotRequired[str]
