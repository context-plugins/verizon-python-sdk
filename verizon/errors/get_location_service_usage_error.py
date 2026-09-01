from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

GetLocationServiceUsageErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _GetLocationServiceUsageError:
    def map(self, response: HttpResponse) -> GetLocationServiceUsageErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceLocationResult](response)
            case _:
                return RawError(response)


get_location_service_usage_error_mapper: Final[
    ErrorMapper[GetLocationServiceUsageErrorBody]
] = _GetLocationServiceUsageError()
