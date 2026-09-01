from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WrongWayDrivingCauseCode(SdkBaseModel):
    """Cause code wrapper for wrong way driving events."""

    wrong_way_driving14: int = Field(alias="wrongWayDriving14")
    """The value shall be set to:
    - 0 ``unavailable`` - in case further detailed information on wrong way driving event is unavailable,
    - 1 ``wrongLane`` - in case vehicle is driving on a lane for which it has no authorization to use,
    - 2 ``wrongDirection`` - in case vehicle is driving in a direction that it is not allowed,
    - 3-255 - reserved for future usage."""


class WrongWayDrivingCauseCodeDict(TypedDict):
    wrong_way_driving14: int
