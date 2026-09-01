from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TheIdresourceandDeviceId(SdkBaseModel):
    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    deviceid: Optional[str] = UNSET
    """This is a UUID value of the device created when the device is onboarded"""


class TheIdresourceandDeviceIdDict(TypedDict):
    id: NotRequired[str]
    deviceid: NotRequired[str]
