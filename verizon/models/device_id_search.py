from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DeviceIdSearch(SdkBaseModel):
    """Search by device id."""

    contains: str
    """The string appears anywhere in the identifer."""

    startswith: Optional[str] = UNSET
    """The identifer must start with the specified string."""

    endswith: Optional[str] = UNSET
    """The identifier must end with the specified string."""

    kind: str
    """The type of the device identifier. Valid types of identifiers are:ESN (decimal),EID,ICCID (up to 20 digits),IMEI
    (up to 16 digits),MDN,MEID (hexadecimal),MSISDN."""


class DeviceIdSearchDict(TypedDict):
    contains: str
    startswith: NotRequired[str]
    endswith: NotRequired[str]
    kind: str
