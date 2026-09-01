from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ConsentDeleteRequest(SdkBaseModel):
    account_name: Optional[str] = Field(default=UNSET, alias="accountName")
    """Account identifier."""

    device_list: Optional[list[str]] = Field(default=UNSET, alias="deviceList")
    """Device ID list."""


class ConsentDeleteRequestDict(TypedDict):
    account_name: NotRequired[str]
    device_list: NotRequired[list[str]]
