from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoAddUsersToNotificationGroupRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    userids: Optional[list[str]] = UNSET


class DtoAddUsersToNotificationGroupRequestDict(TypedDict):
    accountname: NotRequired[str]
    id: NotRequired[str]
    userids: NotRequired[list[str]]
