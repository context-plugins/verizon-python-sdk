from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RoadSignPosition(SdkBaseModel):
    """Precise location of a road sign in the WGS-84 coordinate system, from which short offsets may be used to create
    additional data using a flat earth projection centered on this location."""

    lat: int
    """The geographic latitude of an object, expressed in 1/10th integer microdegrees, as a 31 bit value, and with
    reference to the horizontal datum then in use. The value 900000001 shall be used when unavailable."""

    long: int
    """The geographic longitude of an object, expressed in 1/10th integer microdegrees, as a 32-bit value, and with
    reference to the horizontal datum then in use. The value 1800000001 shall be used when unavailable."""


class RoadSignPositionDict(TypedDict):
    lat: int
    long: int
