from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .offset_system import OffsetSystem, OffsetSystemDict


class GeographicalPathDescription(SdkBaseModel):
    """This data frame can describe a complex path of arbitrary size using node offset method (LL offsets)."""

    path: OffsetSystem
    """The OffsetSystem data frame selects a sequence of node offsets described in the Lat-Long offset method."""


class GeographicalPathDescriptionDict(TypedDict):
    path: OffsetSystem | OffsetSystemDict
