from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DtoOffBoardSensor(SdkBaseModel):
    """The EUI64 address of the device being removed"""

    deveui: Optional[str] = UNSET
    """the IEEE EUI64 address space used to identify a device. It is supplied by the device manufacturer"""


class DtoOffBoardSensorDict(TypedDict):
    deveui: NotRequired[str]
