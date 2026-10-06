from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

CreateListOfLicensesToRemoveErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _CreateListOfLicensesToRemoveError:
    def map(self, status_code: int, content: bytes) -> CreateListOfLicensesToRemoveErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


create_list_of_licenses_to_remove_error_mapper: Final[
    ErrorMapper[CreateListOfLicensesToRemoveErrorBody]
] = _CreateListOfLicensesToRemoveError()
