from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .coordinates import Coordinates, CoordinatesDict


class Locationscoord(SdkBaseModel):
    """Location coordinates."""

    coordinates_list: Optional[list[Coordinates]] = Field(default=UNSET, alias="coordinatesList")


class LocationscoordDict(TypedDict):
    coordinates_list: NotRequired[list[Coordinates | CoordinatesDict]]
