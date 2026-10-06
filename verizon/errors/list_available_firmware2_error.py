from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

ListAvailableFirmware2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _ListAvailableFirmware2Error:
    def map(self, status_code: int, content: bytes) -> ListAvailableFirmware2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


list_available_firmware2_error_mapper: Final[
    ErrorMapper[ListAvailableFirmware2ErrorBody]
] = _ListAvailableFirmware2Error()
