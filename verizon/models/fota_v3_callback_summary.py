from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV3CallbackSummary(SdkBaseModel):
    """Callback registration information."""

    url: Optional[str] = UNSET
    """Callback URL for an subscribed service."""


class FotaV3CallbackSummaryDict(TypedDict):
    url: NotRequired[str]
