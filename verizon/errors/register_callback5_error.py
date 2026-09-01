from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

RegisterCallback5ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback5Error:
    def map(self, response: HttpResponse) -> RegisterCallback5ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


register_callback5_error_mapper: Final[ErrorMapper[RegisterCallback5ErrorBody]] = _RegisterCallback5Error()
