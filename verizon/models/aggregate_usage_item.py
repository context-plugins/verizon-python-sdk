from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AggregateUsageItem(SdkBaseModel):
    """Contains usage information per device."""

    imei: Optional[str] = UNSET
    """The International Mobile Equipment Identifier of the device."""

    number_of_sessions: Optional[int] = Field(default=UNSET, alias="numberOfSessions")
    """Number of sessions established by the device reporting usage."""

    bytes_transferred: Optional[int] = Field(default=UNSET, alias="bytesTransferred")
    """The amount of data transferred by the device reporting usage, measured in Bytes."""


class AggregateUsageItemDict(TypedDict):
    imei: NotRequired[str]
    number_of_sessions: NotRequired[int]
    bytes_transferred: NotRequired[int]
