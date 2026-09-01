from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RetrievesAvailableFilesResponse(SdkBaseModel):
    file_name: Optional[str] = Field(default=UNSET, alias="fileName")
    """ThingSpace-generated name of the file. You will use this name when listing or scheduling campaigns for the
    file."""

    file_version: Optional[str] = Field(default=UNSET, alias="fileVersion")
    """Version of the file."""

    release_note: Optional[str] = Field(default=UNSET, alias="releaseNote")
    """Software release note."""

    make: Optional[str] = UNSET
    """The software-applicable device make."""

    model: Optional[str] = UNSET
    """The software-applicable device model."""

    local_target_path: Optional[str] = Field(default=UNSET, alias="localTargetPath")
    """Local target path on the device."""

    distribution_type: Optional[str] = Field(default=UNSET, alias="distributionType")
    """Valid values"""

    device_platform_id: Optional[str] = Field(default=UNSET, alias="devicePlatformId")
    """The platform (Android, iOS, etc.,) that the software can be applied to."""


class RetrievesAvailableFilesResponseDict(TypedDict):
    file_name: NotRequired[str]
    file_version: NotRequired[str]
    release_note: NotRequired[str]
    make: NotRequired[str]
    model: NotRequired[str]
    local_target_path: NotRequired[str]
    distribution_type: NotRequired[str]
    device_platform_id: NotRequired[str]
