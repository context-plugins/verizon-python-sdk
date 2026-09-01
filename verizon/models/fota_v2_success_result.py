from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FotaV2SuccessResult(SdkBaseModel):
    """Response to a successful request."""

    success: bool


class FotaV2SuccessResultDict(TypedDict):
    success: bool
