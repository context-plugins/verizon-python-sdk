from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .road_sign_id import RoadSignId, RoadSignIdDict


class RoadSignMsgId(SdkBaseModel):
    """Message ID referencing a road sign location."""

    road_sign_id: RoadSignId = Field(alias="roadSignID")
    """It provide a precise location of one or more roadside signs."""


class RoadSignMsgIdDict(TypedDict):
    road_sign_id: RoadSignId | RoadSignIdDict
