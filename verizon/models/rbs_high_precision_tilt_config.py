from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.mode import ModeOrStr
from .periodic_reporting import PeriodicReporting, PeriodicReportingDict
from .tscore import Tscore, TscoreDict


class RbsHighPrecisionTiltConfig(SdkBaseModel):
    mode: Optional[ModeOrStr] = UNSET
    """the reporting mode of the tilt sensor"""

    periodic_reporting: Optional[PeriodicReporting] = Field(default=UNSET, alias="periodic-reporting")
    """The units and values of the time interval for the sensor to send a report"""

    hold_time: Optional[int] = Field(default=UNSET, alias="hold-time")
    """The time the threshold condition exists, in milliseconds, to recognize an event"""

    angle_away: Optional[int] = Field(default=UNSET, alias="angle-away")
    """the threshold value, from verticle, to recognize an event"""

    angle_toward: Optional[int] = Field(default=UNSET, alias="angle-toward")
    """the threshold value, moving towards verticle, to recognize an event"""

    tscore: Optional[Tscore] = UNSET


class RbsHighPrecisionTiltConfigDict(TypedDict):
    mode: NotRequired[ModeOrStr]
    periodic_reporting: NotRequired[PeriodicReporting | PeriodicReportingDict]
    hold_time: NotRequired[int]
    angle_away: NotRequired[int]
    angle_toward: NotRequired[int]
    tscore: NotRequired[Tscore | TscoreDict]
