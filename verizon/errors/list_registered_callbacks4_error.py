from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ListRegisteredCallbacks4ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ListRegisteredCallbacks4Error:
    def map(self, status_code: int, content: bytes) -> ListRegisteredCallbacks4ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV2Result](content)
            case _:
                return RawError(status_code, content)


list_registered_callbacks4_error_mapper: Final[
    ErrorMapper[ListRegisteredCallbacks4ErrorBody]
] = _ListRegisteredCallbacks4Error()
