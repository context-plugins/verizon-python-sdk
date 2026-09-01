from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

UpdateDeviceHyperPreciseStatusErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _UpdateDeviceHyperPreciseStatusError:
    def map(self, response: HttpResponse) -> UpdateDeviceHyperPreciseStatusErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](response)
            case _:
                return RawError(response)


update_device_hyper_precise_status_error_mapper: Final[
    ErrorMapper[UpdateDeviceHyperPreciseStatusErrorBody]
] = _UpdateDeviceHyperPreciseStatusError()
