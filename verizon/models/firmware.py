from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class Firmware(SdkBaseModel):
    """Firmware information."""

    firmware_name: Optional[str] = Field(default=UNSET, alias="firmwareName")
    """The name of the firmware image, provided by the device manufacturer."""

    participant_name: Optional[str] = Field(default=UNSET, alias="participantName")
    """Internal reference; can be ignored."""

    launch_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="launchDate")
    """The release date of the firmware image."""

    release_note: Optional[str] = Field(default=UNSET, alias="releaseNote")
    """Additional information about the release."""

    model: Optional[str] = UNSET
    """The device model that the firmware applies to."""

    make: Optional[str] = UNSET
    """The device make that the firmware applies to."""

    from_version: Optional[str] = Field(default=UNSET, alias="fromVersion")
    """The firmware version that must currently be on the device to upgrade."""

    to_version: Optional[str] = Field(default=UNSET, alias="toVersion")
    """The firmware version that will be on the device after an upgrade."""


class FirmwareDict(TypedDict):
    firmware_name: NotRequired[str]
    participant_name: NotRequired[str]
    launch_date: NotRequired[RFC3339DateTime]
    release_note: NotRequired[str]
    model: NotRequired[str]
    make: NotRequired[str]
    from_version: NotRequired[str]
    to_version: NotRequired[str]
