from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gbidevice_id15 import GbideviceId15, GbideviceId15Dict


class GbideviceIdarray25(SdkBaseModel):
    device_id: Optional[list[GbideviceId15]] = Field(default=UNSET, alias="deviceId")


class GbideviceIdarray25Dict(TypedDict):
    device_id: NotRequired[list[GbideviceId15 | GbideviceId15Dict]]
