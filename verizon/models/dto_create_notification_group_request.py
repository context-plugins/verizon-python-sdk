from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_notification_group_request_entity import (
    DtoNotificationGroupRequestEntity,
    DtoNotificationGroupRequestEntityDict,
)


class DtoCreateNotificationGroupRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    group: DtoNotificationGroupRequestEntity
    userids: Optional[list[str]] = UNSET


class DtoCreateNotificationGroupRequestDict(TypedDict):
    accountname: NotRequired[str]
    group: DtoNotificationGroupRequestEntity | DtoNotificationGroupRequestEntityDict
    userids: NotRequired[list[str]]
