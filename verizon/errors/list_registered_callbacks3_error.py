from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

ListRegisteredCallbacks3ErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _ListRegisteredCallbacks3Error:
    def map(self, status_code: int, content: bytes) -> ListRegisteredCallbacks3ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


list_registered_callbacks3_error_mapper: Final[
    ErrorMapper[ListRegisteredCallbacks3ErrorBody]
] = _ListRegisteredCallbacks3Error()
