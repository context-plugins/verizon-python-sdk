from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

RegisterCallback3ErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback3Error:
    def map(self, status_code: int, content: bytes) -> RegisterCallback3ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


register_callback3_error_mapper: Final[ErrorMapper[RegisterCallback3ErrorBody]] = _RegisterCallback3Error()
