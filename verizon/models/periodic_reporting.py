from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.unit import UnitOrStr


class PeriodicReporting(SdkBaseModel):
    """The units and values of the time interval for the sensor to send a report"""

    unit: Optional[UnitOrStr] = UNSET
    hours: Optional[int] = UNSET
    """whole numbers from 0 to 24"""

    minutes: Optional[int] = UNSET
    """whole numbers from 0 to 59"""


class PeriodicReportingDict(TypedDict):
    unit: NotRequired[UnitOrStr]
    hours: NotRequired[int]
    minutes: NotRequired[int]
