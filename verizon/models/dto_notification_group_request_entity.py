from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoNotificationGroupRequestEntity(SdkBaseModel):
    description: Optional[str] = UNSET
    """a short description"""

    groupemail: Optional[str] = UNSET
    """Contact email for the group"""

    name: Optional[str] = UNSET
    """User defined name of the record"""


class DtoNotificationGroupRequestEntityDict(TypedDict):
    description: NotRequired[str]
    groupemail: NotRequired[str]
    name: NotRequired[str]
