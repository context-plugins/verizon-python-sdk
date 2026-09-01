from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sensorinsightsconfig import Sensorinsightsconfig, SensorinsightsconfigDict


class DtoOffBoardSensorRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    configuration: Optional[Sensorinsightsconfig] = UNSET
    """The configuration of the remove request"""


class DtoOffBoardSensorRequestDict(TypedDict):
    accountname: NotRequired[str]
    configuration: NotRequired[Sensorinsightsconfig | SensorinsightsconfigDict]
