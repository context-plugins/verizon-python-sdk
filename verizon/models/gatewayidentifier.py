from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Gatewayidentifier(SdkBaseModel):
    deviceid: Optional[str] = UNSET
    """a unique parent deviceid used to group all Lora sensors. Sensors need parent gateway for connection"""


class GatewayidentifierDict(TypedDict):
    deviceid: NotRequired[str]
