from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

RegisterCallback2ErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback2Error:
    def map(self, status_code: int, content: bytes) -> RegisterCallback2ErrorBody:
        match status_code:
            case 400:
                return decode_json[DeviceLocationResult](content)
            case _:
                return RawError(status_code, content)


register_callback2_error_mapper: Final[ErrorMapper[RegisterCallback2ErrorBody]] = _RegisterCallback2Error()
