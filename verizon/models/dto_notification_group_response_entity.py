from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .dto_user_dto import DtoUserDto, DtoUserDtoDict


class DtoNotificationGroupResponseEntity(SdkBaseModel):
    createdon: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    description: Optional[str] = UNSET
    """a short description"""

    foreignid: Optional[str] = UNSET
    """UUID of the ECPD account the user belongs to"""

    groupemail: Optional[str] = UNSET
    """Contact email for the group"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    lastupdated: Optional[RFC3339DateTime] = UNSET
    """Timestamp of the record"""

    name: Optional[str] = UNSET
    """User defined name of the record"""

    users: Optional[list[DtoUserDto]] = UNSET
    version: Optional[str] = UNSET
    """The resource version"""

    versionid: Optional[str] = UNSET
    """The UUID of the resource version"""


class DtoNotificationGroupResponseEntityDict(TypedDict):
    createdon: NotRequired[RFC3339DateTime]
    description: NotRequired[str]
    foreignid: NotRequired[str]
    groupemail: NotRequired[str]
    id: NotRequired[str]
    lastupdated: NotRequired[RFC3339DateTime]
    name: NotRequired[str]
    users: NotRequired[list[DtoUserDto | DtoUserDtoDict]]
    version: NotRequired[str]
    versionid: NotRequired[str]
