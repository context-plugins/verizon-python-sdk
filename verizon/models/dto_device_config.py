from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sensor_insights_ble import SensorInsightsBle, SensorInsightsBleDict


class DtoDeviceConfig(SdkBaseModel):
    ble: Optional[SensorInsightsBle] = UNSET
    """Property objects for Bluetooth Low-Energy (BLE) devices"""


class DtoDeviceConfigDict(TypedDict):
    ble: NotRequired[SensorInsightsBle | SensorInsightsBleDict]
