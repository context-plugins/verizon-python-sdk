from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dto_user_dto import DtoUserDto, DtoUserDtoDict


class DtoCreateUserRequest(SdkBaseModel):
    accountname: Optional[str] = UNSET
    """The numeric account name, which must include leading zeros"""

    user: Optional[DtoUserDto] = UNSET


class DtoCreateUserRequestDict(TypedDict):
    accountname: NotRequired[str]
    user: NotRequired[DtoUserDto | DtoUserDtoDict]
