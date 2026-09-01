from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class HeadingRange(SdkBaseModel):
    """Acceptable heading range for road users in degrees."""

    min: float
    """The minimum value of heading in unit of degrees."""

    max: float
    """The maximum value of heading in unit of degrees."""


class HeadingRangeDict(TypedDict):
    min: float
    max: float
