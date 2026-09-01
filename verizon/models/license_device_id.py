from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LicenseDeviceId(SdkBaseModel):
    """Id of the devices."""

    id: Optional[str] = UNSET
    """For 4G devices, IMEI (decimal, up to 15 digits) for unassign and ICCID (decimal, up to 20 digits) for assign."""

    kind: Optional[str] = UNSET
    """For 4G devices, ICCID (decimal, up to 20 digits) for unassign and IMEI (decimal, up to 15 digits) for assign."""


class LicenseDeviceIdDict(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
