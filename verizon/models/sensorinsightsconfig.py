from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_off_board_sensor import DtoOffBoardSensor, DtoOffBoardSensorDict


class Sensorinsightsconfig(SdkBaseModel):
    """The configuration of the remove request"""

    removesensor: Optional[DtoOffBoardSensor] = UNSET
    """The EUI64 address of the device being removed"""


class SensorinsightsconfigDict(TypedDict):
    removesensor: NotRequired[DtoOffBoardSensor | DtoOffBoardSensorDict]
