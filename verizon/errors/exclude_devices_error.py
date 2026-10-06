from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

ExcludeDevicesErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _ExcludeDevicesError:
    def map(self, status_code: int, content: bytes) -> ExcludeDevicesErrorBody:
        match status_code:
            case 400:
                return decode_json[DeviceLocationResult](content)
            case _:
                return RawError(status_code, content)


exclude_devices_error_mapper: Final[ErrorMapper[ExcludeDevicesErrorBody]] = _ExcludeDevicesError()
