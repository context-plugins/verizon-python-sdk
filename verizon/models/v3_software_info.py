from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V3SoftwareInfo(SdkBaseModel):
    """Software information."""

    name: str
    """Software name."""

    version: str
    """Software version."""

    upgrade_time: str = Field(alias="upgradeTime")
    """Upgrade time."""


class V3SoftwareInfoDict(TypedDict):
    name: str
    version: str
    upgrade_time: str
