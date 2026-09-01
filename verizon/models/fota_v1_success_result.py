from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FotaV1SuccessResult(SdkBaseModel):
    """A response to a successful request contains a single Boolean value."""

    success: Optional[bool] = UNSET
    """True is returned in case of success."""


class FotaV1SuccessResultDict(TypedDict):
    success: NotRequired[bool]
