from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class RegionIntersectionPair(SdkBaseModel):
    """Specific region and intersection identification pair"""

    region_id: int = Field(default=0, alias="regionId")
    """The region identifier code (0-65535)"""

    intersection_id: int = Field(alias="intersectionId")
    """The intersection identifier code (0-65535)"""


class RegionIntersectionPairDict(TypedDict):
    region_id: NotRequired[int]
    intersection_id: int
