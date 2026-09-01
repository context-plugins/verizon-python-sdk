from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

DeleteListOfLicensesToRemove2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _DeleteListOfLicensesToRemove2Error:
    def map(self, response: HttpResponse) -> DeleteListOfLicensesToRemove2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


delete_list_of_licenses_to_remove2_error_mapper: Final[
    ErrorMapper[DeleteListOfLicensesToRemove2ErrorBody]
] = _DeleteListOfLicensesToRemove2Error()
