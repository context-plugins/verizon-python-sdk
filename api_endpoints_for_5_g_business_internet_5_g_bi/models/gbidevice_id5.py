from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbidevice_id15 import GbideviceId15, GbideviceId15Dict


class GbideviceId5(SdkBaseModel):
    device_id: Optional[GbideviceId15] = Field(default=UNSET, alias="deviceId")


class GbideviceId5Dict(TypedDict):
    device_id: NotRequired[GbideviceId15 | GbideviceId15Dict]
