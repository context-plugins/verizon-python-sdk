from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .rock import Rock, RockDict


class DescriptionOfRoadSurfaceRock(SdkBaseModel):
    rock: Rock
    """Indicates the surface of the roadway is rock."""


class DescriptionOfRoadSurfaceRockDict(TypedDict):
    rock: Rock | RockDict
