from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type3 import Type3OrStr


class Polygon(SdkBaseModel):
    """A Polygon is a type of geometry that represents a collection of points that form a closed ring.

    NOTE: This API only supports a single polygon in the Polygon geometry, so holes cannot be defines at this point.
    Support for hole will be added in future releases."""

    type_: Type3OrStr = Field(alias="type")
    coordinates: list[list[list[float]]]


class PolygonDict(TypedDict):
    type_: Type3OrStr
    coordinates: list[list[list[float]]]
