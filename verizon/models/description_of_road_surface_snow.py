from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .snow import Snow, SnowDict


class DescriptionOfRoadSurfaceSnow(SdkBaseModel):
    snow: Snow
    """Indicates the surface of the roadway is snow."""


class DescriptionOfRoadSurfaceSnowDict(TypedDict):
    snow: Snow | SnowDict
