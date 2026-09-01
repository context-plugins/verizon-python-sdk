from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ice import Ice, IceDict


class DescriptionOfRoadSurfaceIce(SdkBaseModel):
    ice: Ice
    """Indicates the surface of the roadway is ice."""


class DescriptionOfRoadSurfaceIceDict(TypedDict):
    ice: Ice | IceDict
