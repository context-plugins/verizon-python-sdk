from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeviceId(SdkBaseModel):
    """An identifier for a single device."""

    id: str
    """The value of the device identifier."""

    kind: str
    """The type of the device identifier. Valid types of identifiers are:ESN (decimal),EID,ICCID (up to 20 digits),IMEI
    (up to 16 digits),MDN,MEID (hexadecimal),MSISDN."""


class DeviceIdDict(TypedDict):
    id: str
    kind: str
