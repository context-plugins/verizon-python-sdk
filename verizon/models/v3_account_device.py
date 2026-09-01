from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v3_software_info import V3SoftwareInfo, V3SoftwareInfoDict


class V3AccountDevice(SdkBaseModel):
    """Device information."""

    device_id: str = Field(alias="deviceId")
    """Device identifier."""

    mdn: str
    """MDN."""

    model: str
    """Device model."""

    make: str
    """Device make."""

    firmware: str
    """Device firmware version."""

    fota_eligible: bool = Field(alias="fotaEligible")
    """Value=true if the device software can be upgraded over the air using the Software Management Services API."""

    status: str
    """Device status."""

    license_assigned: bool = Field(alias="licenseAssigned")
    """License assigned device."""

    protocol: str
    """Firmware protocol. Valid values include: LWM2M, OMADM, HTTP or NONE."""

    software_list: list[V3SoftwareInfo] = Field(alias="softwareList")
    """List of sofware."""

    file_list: Optional[list[V3SoftwareInfo]] = Field(default=UNSET, alias="fileList")
    """List of files."""

    create_time: Optional[str] = Field(default=UNSET, alias="createTime")
    """The date and time of when the device is created."""

    upgrade_time: Optional[str] = Field(default=UNSET, alias="upgradeTime")
    """The date and time of when the device firmware or software is updated."""

    update_time: Optional[str] = Field(default=UNSET, alias="updateTime")
    """The date and time of when the device is updated."""

    refresh_time: Optional[str] = Field(default=UNSET, alias="refreshTime")
    """The date and time of when the device is refreshed."""


class V3AccountDeviceDict(TypedDict):
    device_id: str
    mdn: str
    model: str
    make: str
    firmware: str
    fota_eligible: bool
    status: str
    license_assigned: bool
    protocol: str
    software_list: list[V3SoftwareInfo | V3SoftwareInfoDict]
    file_list: NotRequired[list[V3SoftwareInfo | V3SoftwareInfoDict]]
    create_time: NotRequired[str]
    upgrade_time: NotRequired[str]
    update_time: NotRequired[str]
    refresh_time: NotRequired[str]
