from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .resource_on_board_sensor import ResourceOnBoardSensor, ResourceOnBoardSensorDict


class Payload(SdkBaseModel):
    addsensor: Optional[ResourceOnBoardSensor] = UNSET


class PayloadDict(TypedDict):
    addsensor: NotRequired[ResourceOnBoardSensor | ResourceOnBoardSensorDict]
