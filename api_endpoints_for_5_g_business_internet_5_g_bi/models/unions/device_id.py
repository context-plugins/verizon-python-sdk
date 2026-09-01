from __future__ import annotations

from typing import TypeAlias

from ..gbidevice_id15 import GbideviceId15, GbideviceId15Dict

DeviceId: TypeAlias = GbideviceId15 | GbideviceId15

DeviceIdDict: TypeAlias = GbideviceId15Dict | GbideviceId15Dict
