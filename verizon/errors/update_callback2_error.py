from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

UpdateCallback2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCallback2Error:
    def map(self, status_code: int, content: bytes) -> UpdateCallback2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


update_callback2_error_mapper: Final[ErrorMapper[UpdateCallback2ErrorBody]] = _UpdateCallback2Error()
