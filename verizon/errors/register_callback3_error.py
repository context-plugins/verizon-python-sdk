from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

RegisterCallback3ErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback3Error:
    def map(self, response: HttpResponse) -> RegisterCallback3ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV1Result](response)
            case _:
                return RawError(response)


register_callback3_error_mapper: Final[ErrorMapper[RegisterCallback3ErrorBody]] = _RegisterCallback3Error()
