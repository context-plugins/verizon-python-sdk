from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

CreateNewTriggerErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _CreateNewTriggerError:
    def map(self, response: HttpResponse) -> CreateNewTriggerErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceLocationResult](response)
            case _:
                return RawError(response)


create_new_trigger_error_mapper: Final[ErrorMapper[CreateNewTriggerErrorBody]] = _CreateNewTriggerError()
