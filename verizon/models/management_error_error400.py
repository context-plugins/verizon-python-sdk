from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ManagementErrorError400(SdkBaseModel):
    error: Optional[str] = UNSET
    error_description: Optional[str] = UNSET
    cause: Optional[str] = UNSET


class ManagementErrorError400Dict(TypedDict):
    error: NotRequired[str]
    error_description: NotRequired[str]
    cause: NotRequired[str]
