from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceLocationSuccessResult(SdkBaseModel):
    """Whether the device location request was successful or not."""

    success: Optional[bool] = UNSET


class DeviceLocationSuccessResultDict(TypedDict):
    success: NotRequired[bool]
