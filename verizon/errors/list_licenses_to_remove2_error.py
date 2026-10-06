from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ListLicensesToRemove2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ListLicensesToRemove2Error:
    def map(self, status_code: int, content: bytes) -> ListLicensesToRemove2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV2Result](content)
            case _:
                return RawError(status_code, content)


list_licenses_to_remove2_error_mapper: Final[
    ErrorMapper[ListLicensesToRemove2ErrorBody]
] = _ListLicensesToRemove2Error()
