from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoUserDto(SdkBaseModel):
    email: Optional[str] = UNSET
    """Contact email for the group"""

    firstname: Optional[str] = UNSET
    """The first name in the user record"""

    lastname: Optional[str] = UNSET
    """The last name in the user record"""

    mdn: Optional[str] = UNSET
    """The Mobile Directory Number"""

    customdata: Optional[dict[str, Any]] = UNSET
    """Name/value pair, where the value is client defined. The purpose is to keep track of current state per device
    action."""


class DtoUserDtoDict(TypedDict):
    email: NotRequired[str]
    firstname: NotRequired[str]
    lastname: NotRequired[str]
    mdn: NotRequired[str]
    customdata: NotRequired[dict[str, Any]]
