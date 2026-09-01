from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PositionData(SdkBaseModel):
    """Position data."""

    time: Optional[str] = UNSET
    """Time location obtained."""

    utcoffset: Optional[str] = UNSET
    """UTC offset of time."""

    x: Optional[str] = UNSET
    """X coordinate of location."""

    y: Optional[str] = UNSET
    """Y coordinate of location."""

    radius: Optional[str] = UNSET
    """Radius of the location in meters."""

    qos: Optional[bool] = UNSET
    """Whether requested accurary is met or not."""


class PositionDataDict(TypedDict):
    time: NotRequired[str]
    utcoffset: NotRequired[str]
    x: NotRequired[str]
    y: NotRequired[str]
    radius: NotRequired[str]
    qos: NotRequired[bool]
