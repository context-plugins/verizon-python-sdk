from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type5 import Type5OrStr


class MultiPolygon(SdkBaseModel):
    """A MultiPolygon is a type of geometry that represents a collection of Polygon geometries."""

    type_: Type5OrStr = Field(alias="type")
    coordinates: list[list[list[list[float]]]]


class MultiPolygonDict(TypedDict):
    type_: Type5OrStr
    coordinates: list[list[list[list[float]]]]
