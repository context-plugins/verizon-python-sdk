from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .altitude import Altitude, AltitudeDict
from .pos_confidence_ellipse import PosConfidenceEllipse, PosConfidenceEllipseDict


class EventPosition(SdkBaseModel):
    latitude: int
    """Latitude of the event location in microdegrees (900000001 shall be used when unavailable)."""

    longitude: int
    """Longitude of the event location in microdegrees (1800000001 shall be used when unavailable)."""

    position_confidence_ellipse: PosConfidenceEllipse = Field(alias="positionConfidenceEllipse")
    altitude: Altitude


class EventPositionDict(TypedDict):
    latitude: int
    longitude: int
    position_confidence_ellipse: PosConfidenceEllipse | PosConfidenceEllipseDict
    altitude: Altitude | AltitudeDict
