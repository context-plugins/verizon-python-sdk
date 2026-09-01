from __future__ import annotations

from typing import TypeAlias

from ..description_of_road_surface_asphalt_or_tar import (
    DescriptionOfRoadSurfaceAsphaltOrTar,
    DescriptionOfRoadSurfaceAsphaltOrTarDict,
)
from ..description_of_road_surface_cinders import DescriptionOfRoadSurfaceCinders, DescriptionOfRoadSurfaceCindersDict
from ..description_of_road_surface_grass import DescriptionOfRoadSurfaceGrass, DescriptionOfRoadSurfaceGrassDict
from ..description_of_road_surface_gravel import DescriptionOfRoadSurfaceGravel, DescriptionOfRoadSurfaceGravelDict
from ..description_of_road_surface_ice import DescriptionOfRoadSurfaceIce, DescriptionOfRoadSurfaceIceDict
from ..description_of_road_surface_portland_cement import (
    DescriptionOfRoadSurfacePortlandCement,
    DescriptionOfRoadSurfacePortlandCementDict,
)
from ..description_of_road_surface_rock import DescriptionOfRoadSurfaceRock, DescriptionOfRoadSurfaceRockDict
from ..description_of_road_surface_snow import DescriptionOfRoadSurfaceSnow, DescriptionOfRoadSurfaceSnowDict

DescriptionOfRoadSurface: TypeAlias = (
    DescriptionOfRoadSurfacePortlandCement
    | DescriptionOfRoadSurfaceAsphaltOrTar
    | DescriptionOfRoadSurfaceGravel
    | DescriptionOfRoadSurfaceGrass
    | DescriptionOfRoadSurfaceCinders
    | DescriptionOfRoadSurfaceRock
    | DescriptionOfRoadSurfaceIce
    | DescriptionOfRoadSurfaceSnow
)
"""Indicates the composition of the surface of the roadway for use in estimation of friction."""

DescriptionOfRoadSurfaceDict: TypeAlias = (
    DescriptionOfRoadSurfacePortlandCementDict
    | DescriptionOfRoadSurfaceAsphaltOrTarDict
    | DescriptionOfRoadSurfaceGravelDict
    | DescriptionOfRoadSurfaceGrassDict
    | DescriptionOfRoadSurfaceCindersDict
    | DescriptionOfRoadSurfaceRockDict
    | DescriptionOfRoadSurfaceIceDict
    | DescriptionOfRoadSurfaceSnowDict
)
