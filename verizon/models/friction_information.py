from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.description_of_road_surface import DescriptionOfRoadSurface, DescriptionOfRoadSurfaceDict


class FrictionInformation(SdkBaseModel):
    road_surface_description: DescriptionOfRoadSurface = Field(alias="roadSurfaceDescription")
    """Indicates the composition of the surface of the roadway for use in estimation of friction."""


class FrictionInformationDict(TypedDict):
    road_surface_description: DescriptionOfRoadSurface | DescriptionOfRoadSurfaceDict
