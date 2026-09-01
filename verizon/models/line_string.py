from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type2 import Type2OrStr


class LineString(SdkBaseModel):
    """A LineString is a type of geometry that represents a collection of points that are connected by line segments."""

    type_: Type2OrStr = Field(alias="type")
    coordinates: list[list[float]]


class LineStringDict(TypedDict):
    type_: Type2OrStr
    coordinates: list[list[float]]
