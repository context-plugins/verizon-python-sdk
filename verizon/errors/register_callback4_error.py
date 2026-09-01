from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

RegisterCallback4ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback4Error:
    def map(self, response: HttpResponse) -> RegisterCallback4ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


register_callback4_error_mapper: Final[ErrorMapper[RegisterCallback4ErrorBody]] = _RegisterCallback4Error()
