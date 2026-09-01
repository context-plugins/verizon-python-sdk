from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PropertyDeviceId(SdkBaseModel):
    id: Optional[str] = UNSET
    kind: Optional[str] = UNSET
    """The type of the device identifier. Valid types of identifiers are:ESN (decimal),EID,ICCID (up to 20 digits),IMEI
    (up to 16 digits),MDN,MEID (hexadecimal),MSISDN."""


class PropertyDeviceIdDict(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
