from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV3CallbackRegistrationResult(SdkBaseModel):
    """Callback registration information."""

    url: Optional[str] = UNSET
    """Callback URL."""


class FotaV3CallbackRegistrationResultDict(TypedDict):
    url: NotRequired[str]
