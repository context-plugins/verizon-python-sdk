from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

AddDevicesHyperPreciseErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _AddDevicesHyperPreciseError:
    def map(self, response: HttpResponse) -> AddDevicesHyperPreciseErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 405 | 406 | 429 | 500:
                return decode_json[HyperPreciseLocationResult](response)
            case _:
                return RawError(response)


add_devices_hyper_precise_error_mapper: Final[
    ErrorMapper[AddDevicesHyperPreciseErrorBody]
] = _AddDevicesHyperPreciseError()
