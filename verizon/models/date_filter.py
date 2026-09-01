from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DateFilter(SdkBaseModel):
    """Filter out the dates."""

    earliest: str
    """Only include devices that were added after this date and time."""

    latest: str
    """Only include devices that were added before this date and time."""


class DateFilterDict(TypedDict):
    earliest: str
    latest: str
