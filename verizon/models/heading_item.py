from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .heading_range import HeadingRange, HeadingRangeDict


class HeadingItem(SdkBaseModel):
    """Heading limitation provides minimum and maximum value for road user heading in unit of degrees. If the road
    user's heading value is between the given minimum and maximum value and the TriggerConditions are also met the
    message will be sent out.

    The heading minimum value can be bigger than the maximum value as negative number are not supported. For example,
    the +/- 10 degrees around the north (0 degrees) can be defined as 350 (min) to 10 (max) degrees."""

    heading: HeadingRange | None
    """Acceptable heading range for road users in degrees."""


class HeadingItemDict(TypedDict):
    heading: HeadingRange | HeadingRangeDict | None
