from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.hyper_precise_location_result import HyperPreciseLocationResult

ListRegisteredCallbacks6ErrorBody: TypeAlias = HyperPreciseLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _ListRegisteredCallbacks6Error:
    def map(self, status_code: int, content: bytes) -> ListRegisteredCallbacks6ErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 409 | 500:
                return decode_json[HyperPreciseLocationResult](content)
            case _:
                return RawError(status_code, content)


list_registered_callbacks6_error_mapper: Final[
    ErrorMapper[ListRegisteredCallbacks6ErrorBody]
] = _ListRegisteredCallbacks6Error()
