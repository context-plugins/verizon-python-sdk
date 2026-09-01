from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .v3_software_info import V3SoftwareInfo, V3SoftwareInfoDict


class V3Device(SdkBaseModel):
    """Device information."""

    device_id: str = Field(alias="deviceId")
    """Device IMEI."""

    request_status: Optional[str] = Field(default=UNSET, alias="requestStatus")
    """Success or failure."""

    result_reason: Optional[str] = Field(default=UNSET, alias="resultReason")
    mdn: Optional[str] = UNSET
    """MDN."""

    model: Optional[str] = UNSET
    """Device model."""

    make: Optional[str] = UNSET
    """Device make."""

    firmware: Optional[str] = UNSET
    """Device firmware version."""

    fota_eligible: Optional[bool] = Field(default=UNSET, alias="fotaEligible")
    """Value=true if the device software can be upgraded over the air using the Software Management Services API."""

    status: Optional[str] = UNSET
    """Device status."""

    license_assigned: Optional[bool] = Field(default=UNSET, alias="licenseAssigned")
    """License assigned device."""

    protocol: Optional[str] = UNSET
    """Firmware protocol. Valid values include: LWM2M, OMADM, HTTP or NONE."""

    software_list: Optional[list[V3SoftwareInfo]] = Field(default=UNSET, alias="softwareList")
    """List of sofware."""

    file_list: Optional[list[V3SoftwareInfo]] = Field(default=UNSET, alias="fileList")
    """List of files."""

    create_time: Optional[str] = Field(default=UNSET, alias="createTime")
    """The date and time of when the device is created."""

    status_time: Optional[str] = Field(default=UNSET, alias="statusTime")
    """The date and time of when the device firmware or software is updated."""

    update_time: Optional[str] = Field(default=UNSET, alias="updateTime")
    """The date and time of when the device is updated."""

    refresh_time: Optional[str] = Field(default=UNSET, alias="refreshTime")
    """The date and time of when the device is refreshed."""

    last_connection_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastConnectionTime")
    """The date and time of when the device reachability is checked."""


class V3DeviceDict(TypedDict):
    device_id: str
    request_status: NotRequired[str]
    result_reason: NotRequired[str]
    mdn: NotRequired[str]
    model: NotRequired[str]
    make: NotRequired[str]
    firmware: NotRequired[str]
    fota_eligible: NotRequired[bool]
    status: NotRequired[str]
    license_assigned: NotRequired[bool]
    protocol: NotRequired[str]
    software_list: NotRequired[list[V3SoftwareInfo | V3SoftwareInfoDict]]
    file_list: NotRequired[list[V3SoftwareInfo | V3SoftwareInfoDict]]
    create_time: NotRequired[str]
    status_time: NotRequired[str]
    update_time: NotRequired[str]
    refresh_time: NotRequired[str]
    last_connection_time: NotRequired[RFC3339DateTime]
