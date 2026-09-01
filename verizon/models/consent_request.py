from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConsentRequest(SdkBaseModel):
    account_name: str = Field(alias="accountName")
    """Account identifier in "##########-#####"."""

    all_device: Optional[bool] = Field(default=UNSET, alias="allDevice")
    """Exclude all devices or not."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The change to make: append or replace."""

    exclusion: Optional[list[str]] = UNSET
    """Device ID list."""


class ConsentRequestDict(TypedDict):
    account_name: str
    all_device: NotRequired[bool]
    type_: NotRequired[str]
    exclusion: NotRequired[list[str]]
