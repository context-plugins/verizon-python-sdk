from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class IntelligenceSuccessResult(SdkBaseModel):
    """Success response."""

    status: Optional[str] = UNSET
    """Anomaly detection status."""


class IntelligenceSuccessResultDict(TypedDict):
    status: NotRequired[str]
