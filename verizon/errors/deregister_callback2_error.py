from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

DeregisterCallback2ErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _DeregisterCallback2Error:
    def map(self, response: HttpResponse) -> DeregisterCallback2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceLocationResult](response)
            case _:
                return RawError(response)


deregister_callback2_error_mapper: Final[ErrorMapper[DeregisterCallback2ErrorBody]] = _DeregisterCallback2Error()
