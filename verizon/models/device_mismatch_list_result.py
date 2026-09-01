from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .mismatched_device import MismatchedDevice, MismatchedDeviceDict


class DeviceMismatchListResult(SdkBaseModel):
    """Response to list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware)
    during a specified time frame."""

    devices: Optional[list[MismatchedDevice]] = UNSET
    """A list of specific devices that you want to check, specified by ICCID or MDN."""


class DeviceMismatchListResultDict(TypedDict):
    devices: NotRequired[list[MismatchedDevice | MismatchedDeviceDict]]
