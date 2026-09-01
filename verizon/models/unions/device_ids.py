from __future__ import annotations

from typing import TypeAlias

from ..device_id import DeviceId, DeviceIdDict

DeviceIds: TypeAlias = list[DeviceId] | DeviceId
"""One object per device to be deleted. Each object must contain a kind and id element identifying the device."""

DeviceIdsDict: TypeAlias = list[DeviceIdDict] | DeviceIdDict
