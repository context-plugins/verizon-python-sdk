from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class UploadConfigurationFilesResponse(SdkBaseModel):
    file_name: Optional[str] = Field(default=UNSET, alias="fileName")
    """The name of the file you are upgrading to."""

    file_version: Optional[str] = Field(default=UNSET, alias="fileVersion")
    """The version of the file you are upgrading to."""

    launch_date: Optional[Date] = Field(default=UNSET, alias="launchDate")
    """Software launch date."""

    release_note: Optional[str] = Field(default=UNSET, alias="releaseNote")
    """Software release note."""

    model: Optional[str] = UNSET
    """Software applicable device model."""

    make: Optional[str] = UNSET
    """Software applicable device make."""

    distribution_type: Optional[str] = Field(default=UNSET, alias="distributionType")
    """LWM2M, OMD-DM or HTTP."""

    device_platform_id: Optional[str] = Field(default=UNSET, alias="devicePlatformId")
    """The platform (Android, iOS, etc.) that the software can be applied to."""

    local_target_path: Optional[str] = Field(default=UNSET, alias="localTargetPath")
    """Local target path on the device."""


class UploadConfigurationFilesResponseDict(TypedDict):
    file_name: NotRequired[str]
    file_version: NotRequired[str]
    launch_date: NotRequired[Date]
    release_note: NotRequired[str]
    model: NotRequired[str]
    make: NotRequired[str]
    distribution_type: NotRequired[str]
    device_platform_id: NotRequired[str]
    local_target_path: NotRequired[str]
