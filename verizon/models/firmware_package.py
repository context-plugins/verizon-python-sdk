from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .enums.campaign_meta_info_protocol import CampaignMetaInfoProtocolOrStr


class FirmwarePackage(SdkBaseModel):
    """Available firmware."""

    firmware_name: str = Field(alias="firmwareName")
    """Firmware name."""

    firmware_from: str = Field(alias="firmwareFrom")
    """Firmware from version."""

    firmware_to: str = Field(alias="firmwareTo")
    """Firmware to version."""

    launch_date: RFC3339DateTime = Field(alias="launchDate")
    """Firmware launch date."""

    release_note: str = Field(alias="releaseNote")
    """Firmware release note."""

    model: str
    """Firmware applicable device model."""

    make: str
    """Firmware applicable device make."""

    protocol: CampaignMetaInfoProtocolOrStr
    """Firmware protocol. Valid values include: LWM2M, OMD-DM."""


class FirmwarePackageDict(TypedDict):
    firmware_name: str
    firmware_from: str
    firmware_to: str
    launch_date: RFC3339DateTime
    release_note: str
    model: str
    make: str
    protocol: CampaignMetaInfoProtocolOrStr
