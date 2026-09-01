from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

DeregisterCallback6ErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _DeregisterCallback6Error:
    def map(self, response: HttpResponse) -> DeregisterCallback6ErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](response)
            case _:
                return RawError(response)


deregister_callback6_error_mapper: Final[ErrorMapper[DeregisterCallback6ErrorBody]] = _DeregisterCallback6Error()
