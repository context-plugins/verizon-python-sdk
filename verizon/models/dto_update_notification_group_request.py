from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_notification_group_request_entity import (
    DtoNotificationGroupRequestEntity,
    DtoNotificationGroupRequestEntityDict,
)


class DtoUpdateNotificationGroupRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    group: DtoNotificationGroupRequestEntity
    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    userids: Optional[list[str]] = UNSET


class DtoUpdateNotificationGroupRequestDict(TypedDict):
    accountname: NotRequired[str]
    group: DtoNotificationGroupRequestEntity | DtoNotificationGroupRequestEntityDict
    id: NotRequired[str]
    userids: NotRequired[list[str]]
