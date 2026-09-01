from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type1 import Type1OrStr
from .unions.geometry import Geometry, GeometryDict


class FeatureItem(SdkBaseModel):
    type_: Type1OrStr = Field(alias="type")
    geometry: Geometry
    properties: Any
    """Properties object for a GeoJSON Feature (no additional properties allowed)."""


class FeatureItemDict(TypedDict):
    type_: Type1OrStr
    geometry: Geometry | GeometryDict
    properties: Any
