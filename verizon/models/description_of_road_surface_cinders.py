from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cinders import Cinders, CindersDict


class DescriptionOfRoadSurfaceCinders(SdkBaseModel):
    cinders: Cinders
    """Indicates the surface of the roadway is cinders."""


class DescriptionOfRoadSurfaceCindersDict(TypedDict):
    cinders: Cinders | CindersDict
