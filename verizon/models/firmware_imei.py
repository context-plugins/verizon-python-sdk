from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FirmwareImei(SdkBaseModel):
    """A list of IMEIs for devices to be synchronized between ThingSpace and the FOTA server."""

    device_list: list[str] = Field(alias="deviceList")
    """Device IMEI list."""


class FirmwareImeiDict(TypedDict):
    device_list: list[str]
