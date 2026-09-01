from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .gravel import Gravel, GravelDict


class DescriptionOfRoadSurfaceGravel(SdkBaseModel):
    gravel: Gravel
    """Indicates the surface of the roadway is gravel."""


class DescriptionOfRoadSurfaceGravelDict(TypedDict):
    gravel: Gravel | GravelDict
