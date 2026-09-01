from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_firmware_version import DeviceFirmwareVersion, DeviceFirmwareVersionDict


class DeviceFirmwareList(SdkBaseModel):
    """Device Firmware Information."""

    account_name: str = Field(alias="accountName")
    """Account name."""

    device_firmwar_version_list: Optional[list[DeviceFirmwareVersion]] = Field(
        default=UNSET, alias="deviceFirmwarVersionList"
    )
    """List of device & firmware."""


class DeviceFirmwareListDict(TypedDict):
    account_name: str
    device_firmwar_version_list: NotRequired[list[DeviceFirmwareVersion | DeviceFirmwareVersionDict]]
