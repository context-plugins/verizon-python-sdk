from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Smsnumber(SdkBaseModel):
    """Notification SMS details."""

    carrier: Optional[str] = UNSET
    number: Optional[str] = UNSET


class SmsnumberDict(TypedDict):
    carrier: NotRequired[str]
    number: NotRequired[str]
