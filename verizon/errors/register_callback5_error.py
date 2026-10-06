from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

RegisterCallback5ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _RegisterCallback5Error:
    def map(self, status_code: int, content: bytes) -> RegisterCallback5ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


register_callback5_error_mapper: Final[ErrorMapper[RegisterCallback5ErrorBody]] = _RegisterCallback5Error()
