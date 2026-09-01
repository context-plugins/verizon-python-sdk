from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FotaV3SuccessResult(SdkBaseModel):
    """Cancelation status."""

    success: bool
    """True or false."""


class FotaV3SuccessResultDict(TypedDict):
    success: bool
