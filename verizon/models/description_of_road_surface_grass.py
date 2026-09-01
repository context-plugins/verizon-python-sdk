from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .grass import Grass, GrassDict


class DescriptionOfRoadSurfaceGrass(SdkBaseModel):
    grass: Grass
    """Indicates the surface of the roadway is grass."""


class DescriptionOfRoadSurfaceGrassDict(TypedDict):
    grass: Grass | GrassDict
