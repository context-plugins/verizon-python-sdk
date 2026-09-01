from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoDeleteNotificationGroupRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    force: Optional[bool] = UNSET
    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""


class DtoDeleteNotificationGroupRequestDict(TypedDict):
    accountname: NotRequired[str]
    force: NotRequired[bool]
    id: NotRequired[str]
