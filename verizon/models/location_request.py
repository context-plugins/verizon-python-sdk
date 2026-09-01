from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_info import DeviceInfo, DeviceInfoDict
from .enums.accuracy_mode import AccuracyModeOrStr
from .enums.cache_mode import CacheModeOrStr


class LocationRequest(SdkBaseModel):
    """The body contains the the account name and list of devices that you want to locate, plus other options."""

    account_name: str = Field(alias="accountName")
    """Account identifier in "##########-#####"."""

    device_list: list[DeviceInfo] = Field(alias="deviceList")
    """Device list."""

    accuracy_mode: Optional[AccuracyModeOrStr] = Field(default=UNSET, alias="accuracyMode")
    """Accurary, currently only 0-coarse supported."""

    cache_mode: Optional[CacheModeOrStr] = Field(default=UNSET, alias="cacheMode")
    """Location cache mode."""


class LocationRequestDict(TypedDict):
    account_name: str
    device_list: list[DeviceInfo | DeviceInfoDict]
    accuracy_mode: NotRequired[AccuracyModeOrStr]
    cache_mode: NotRequired[CacheModeOrStr]
