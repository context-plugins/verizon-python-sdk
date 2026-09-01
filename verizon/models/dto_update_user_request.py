from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_user_dto import DtoUserDto, DtoUserDtoDict


class DtoUpdateUserRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    id: Optional[str] = UNSET
    """UUID of the user record, assigned at creation"""

    user: Optional[DtoUserDto] = UNSET


class DtoUpdateUserRequestDict(TypedDict):
    accountname: NotRequired[str]
    id: NotRequired[str]
    user: NotRequired[DtoUserDto | DtoUserDtoDict]
