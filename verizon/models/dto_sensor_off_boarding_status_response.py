from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_sensor_boarding_event import DtoSensorBoardingEvent, DtoSensorBoardingEventDict


class DtoSensorOffBoardingStatusResponse(SdkBaseModel):
    events: Optional[list[DtoSensorBoardingEvent]] = UNSET
    isstillregistered: Optional[bool] = UNSET


class DtoSensorOffBoardingStatusResponseDict(TypedDict):
    events: NotRequired[list[DtoSensorBoardingEvent | DtoSensorBoardingEventDict]]
    isstillregistered: NotRequired[bool]
