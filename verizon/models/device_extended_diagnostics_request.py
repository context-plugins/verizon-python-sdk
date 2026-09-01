from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_id import DeviceId, DeviceIdDict


class DeviceExtendedDiagnosticsRequest(SdkBaseModel):
    """Request for obtaining device extended diagnostics."""

    account_name: str = Field(alias="accountName")
    """The Verizon billing account that the device belongs to. An account name is usually numeric, and must include any
    leading zeros."""

    device_list: list[DeviceId] = Field(alias="deviceList")
    """The device for which you want diagnostic information, specified by the device's MDN."""


class DeviceExtendedDiagnosticsRequestDict(TypedDict):
    account_name: str
    device_list: list[DeviceId | DeviceIdDict]
