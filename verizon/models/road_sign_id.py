from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .road_sign_position import RoadSignPosition, RoadSignPositionDict


class RoadSignId(SdkBaseModel):
    """It provide a precise location of one or more roadside signs."""

    position: RoadSignPosition
    """Precise location of a road sign in the WGS-84 coordinate system, from which short offsets may be used to create
    additional data using a flat earth projection centered on this location."""

    view_angle: str = Field(alias="viewAngle")
    """OctetStrings are described as hexadecimal strings, where each octet is represented by two hexadecimal
    characters."""


class RoadSignIdDict(TypedDict):
    position: RoadSignPosition | RoadSignPositionDict
    view_angle: str
