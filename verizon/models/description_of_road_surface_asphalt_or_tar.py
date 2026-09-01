from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .asphalt_or_tar import AsphaltOrTar, AsphaltOrTarDict


class DescriptionOfRoadSurfaceAsphaltOrTar(SdkBaseModel):
    asphalt_or_tar: AsphaltOrTar = Field(alias="asphaltOrTar")
    """Indicates the surface of the roadway is asphalt or tar."""


class DescriptionOfRoadSurfaceAsphaltOrTarDict(TypedDict):
    asphalt_or_tar: AsphaltOrTar | AsphaltOrTarDict
