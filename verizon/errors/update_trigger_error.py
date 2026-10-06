from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

UpdateTriggerErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _UpdateTriggerError:
    def map(self, status_code: int, content: bytes) -> UpdateTriggerErrorBody:
        match status_code:
            case 400:
                return decode_json[DeviceLocationResult](content)
            case _:
                return RawError(status_code, content)


update_trigger_error_mapper: Final[ErrorMapper[UpdateTriggerErrorBody]] = _UpdateTriggerError()
