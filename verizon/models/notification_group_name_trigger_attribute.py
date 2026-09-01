from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class NotificationGroupNameTriggerAttribute(SdkBaseModel):
    """Notification group name trigger attribute."""

    key: Optional[str] = UNSET
    """If present, the NotificationGroupName will be listed here."""


class NotificationGroupNameTriggerAttributeDict(TypedDict):
    key: NotRequired[str]
