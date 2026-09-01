from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetPwnperformanceConsentResponse(SdkBaseModel):
    """PWN Performance Consent Response"""

    consent: Optional[str] = UNSET
    """PWN Performance Consent Response."""


class GetPwnperformanceConsentResponseDict(TypedDict):
    consent: NotRequired[str]
