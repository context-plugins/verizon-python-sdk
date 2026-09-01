from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class SoftwarePackage(SdkBaseModel):
    """Software package information."""

    software_name: str = Field(alias="softwareName")
    """Software name."""

    launch_date: Date = Field(alias="launchDate")
    """Software launch date."""

    release_note: Optional[str] = Field(default=UNSET, alias="releaseNote")
    """Software release note reserved for future use."""

    model: str
    """Software applicable device model."""

    make: str
    """Software applicable device make."""

    distribution_type: str = Field(alias="distributionType")
    """LWM2M, OMD-DM or HTTP."""

    device_platform_id: str = Field(alias="devicePlatformId")
    """The platform (Android, iOS, etc.) that the software can be applied to."""


class SoftwarePackageDict(TypedDict):
    software_name: str
    launch_date: Date
    release_note: NotRequired[str]
    model: str
    make: str
    distribution_type: str
    device_platform_id: str
