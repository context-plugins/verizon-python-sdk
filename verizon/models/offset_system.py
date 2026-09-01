from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .offset import Offset, OffsetDict


class OffsetSystem(SdkBaseModel):
    """The OffsetSystem data frame selects a sequence of node offsets described in the Lat-Long offset method."""

    offset: Offset
    """The sequence of node offsets then describes a path or polygon in the Lat-Long system."""


class OffsetSystemDict(TypedDict):
    offset: Offset | OffsetDict
