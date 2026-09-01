from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CallbackSummary(SdkBaseModel):
    """Registered callback information."""

    url: Optional[str] = UNSET
    """Callback URL for an subscribed service."""


class CallbackSummaryDict(TypedDict):
    url: NotRequired[str]
