from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConnectivityManagementSuccessResult(SdkBaseModel):
    """Response to successful request."""

    success: Optional[bool] = UNSET
    """A value of “true” indicates that the device group was created successfully."""


class ConnectivityManagementSuccessResultDict(TypedDict):
    success: NotRequired[bool]
