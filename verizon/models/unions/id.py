from __future__ import annotations

from typing import TypeAlias

from ..device_id import DeviceId, DeviceIdDict
from ..property_device_id import PropertyDeviceId, PropertyDeviceIdDict

Id: TypeAlias = DeviceId | PropertyDeviceId

IdDict: TypeAlias = DeviceIdDict | PropertyDeviceIdDict
