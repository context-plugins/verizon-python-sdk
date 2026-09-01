from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .position_data import PositionData, PositionDataDict
from .position_error import PositionError, PositionErrorDict


class Location(SdkBaseModel):
    """Device location information."""

    msid: Optional[str] = UNSET
    """MDN."""

    pd: Optional[PositionData] = UNSET
    """Position data."""

    error: Optional[PositionError] = UNSET
    """Position error."""


class LocationDict(TypedDict):
    msid: NotRequired[str]
    pd: NotRequired[PositionData | PositionDataDict]
    error: NotRequired[PositionError | PositionErrorDict]
