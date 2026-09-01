from __future__ import annotations

from typing import TypeAlias

from ..device_id2 import DeviceId2, DeviceId2Dict
from ..e_simdevice_id import ESimdeviceId, ESimdeviceIdDict

Id1: TypeAlias = ESimdeviceId | DeviceId2

Id1Dict: TypeAlias = ESimdeviceIdDict | DeviceId2Dict
