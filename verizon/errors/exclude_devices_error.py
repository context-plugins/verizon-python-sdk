from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

ExcludeDevicesErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _ExcludeDevicesError:
    def map(self, response: HttpResponse) -> ExcludeDevicesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceLocationResult](response)
            case _:
                return RawError(response)


exclude_devices_error_mapper: Final[ErrorMapper[ExcludeDevicesErrorBody]] = _ExcludeDevicesError()
