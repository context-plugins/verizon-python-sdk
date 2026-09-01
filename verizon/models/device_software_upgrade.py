from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, SdkBaseModel


class DeviceSoftwareUpgrade(SdkBaseModel):
    """Array of software upgrade objects with the specified status."""

    device_id: str = Field(alias="deviceId")
    """Device identifier."""

    id: str
    """Upgrade identifier."""

    account_name: str = Field(alias="accountName")
    """Account identifier."""

    software_name: Optional[str] = Field(default=UNSET, alias="softwareName")
    """Software name."""

    start_date: Date = Field(alias="startDate")
    """Software upgrade start date."""

    status: str
    """Software upgrade status."""

    reason: str
    """Software upgrade result reason."""


class DeviceSoftwareUpgradeDict(TypedDict):
    device_id: str
    id: str
    account_name: str
    software_name: NotRequired[str]
    start_date: Date
    status: str
    reason: str
