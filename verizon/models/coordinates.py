from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Coordinates(SdkBaseModel):
    """Coordinates information."""

    latitude: Optional[str] = UNSET
    """Latitude value of location."""

    longitude: Optional[str] = UNSET
    """Longitude value of location."""


class CoordinatesDict(TypedDict):
    latitude: NotRequired[str]
    longitude: NotRequired[str]
