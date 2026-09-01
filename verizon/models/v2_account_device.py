from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .v2_software_info import V2SoftwareInfo, V2SoftwareInfoDict


class V2AccountDevice(SdkBaseModel):
    """Account device information."""

    device_id: str = Field(alias="deviceId")
    """Device identifier."""

    mdn: str
    """MDN."""

    model: str
    """Device model."""

    make: str
    """Device make."""

    fota_eligible: bool = Field(alias="fotaEligible")
    """Device FOTA capable."""

    app_fota_eligible: bool = Field(alias="appFotaEligible")
    """Device application FOTA capable."""

    license_assigned: bool = Field(alias="licenseAssigned")
    """License assigned device."""

    distribution_type: str = Field(alias="distributionType")
    """LWM2M, OMD-DM or HTTP."""

    software_list: list[V2SoftwareInfo] = Field(alias="softwareList")
    """List of sofware."""

    create_time: Optional[str] = Field(default=UNSET, alias="createTime")
    """The date and time of when the device is created."""

    upgrade_time: Optional[str] = Field(default=UNSET, alias="upgradeTime")
    """The date and time of when the device firmware or software is upgraded."""

    update_time: Optional[str] = Field(default=UNSET, alias="updateTime")
    """The date and time of when the device is updated."""

    refresh_time: Optional[str] = Field(default=UNSET, alias="refreshTime")
    """The date and time of when the device is refreshed."""


class V2AccountDeviceDict(TypedDict):
    device_id: str
    mdn: str
    model: str
    make: str
    fota_eligible: bool
    app_fota_eligible: bool
    license_assigned: bool
    distribution_type: str
    software_list: list[V2SoftwareInfo | V2SoftwareInfoDict]
    create_time: NotRequired[str]
    upgrade_time: NotRequired[str]
    update_time: NotRequired[str]
    refresh_time: NotRequired[str]
