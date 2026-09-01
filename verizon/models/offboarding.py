from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Offboarding(SdkBaseModel):
    sensoridentifier: Optional[str] = UNSET
    """the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer"""


class OffboardingDict(TypedDict):
    sensoridentifier: NotRequired[str]
