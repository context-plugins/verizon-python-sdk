from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type4 import Type4OrStr


class MultiLineString(SdkBaseModel):
    """A MultiLineString is a type of geometry that represents a collection of LineString geometries."""

    type_: Type4OrStr = Field(alias="type")
    coordinates: list[list[list[float]]]


class MultiLineStringDict(TypedDict):
    type_: Type4OrStr
    coordinates: list[list[list[float]]]
