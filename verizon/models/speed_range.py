from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SpeedRange(SdkBaseModel):
    """Acceptable speed range for road users in m/s."""

    min: float
    """The minimum required speed in m/s."""

    max: float
    """The maximum acceptable speed in m/s."""


class SpeedRangeDict(TypedDict):
    min: float
    max: float
