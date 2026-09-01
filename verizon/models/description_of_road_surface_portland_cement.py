from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .portland_cement import PortlandCement, PortlandCementDict


class DescriptionOfRoadSurfacePortlandCement(SdkBaseModel):
    portland_cement: PortlandCement = Field(alias="portlandCement")
    """Indicates the surface of the roadway is portland cement."""


class DescriptionOfRoadSurfacePortlandCementDict(TypedDict):
    portland_cement: PortlandCement | PortlandCementDict
