from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

RegisterCallback6ErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback6Error:
    def map(self, response: HttpResponse) -> RegisterCallback6ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](response)
            case _:
                return RawError(response)


register_callback6_error_mapper: Final[ErrorMapper[RegisterCallback6ErrorBody]] = _RegisterCallback6Error()
