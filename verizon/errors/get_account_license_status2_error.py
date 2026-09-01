from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

GetAccountLicenseStatus2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountLicenseStatus2Error:
    def map(self, response: HttpResponse) -> GetAccountLicenseStatus2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


get_account_license_status2_error_mapper: Final[
    ErrorMapper[GetAccountLicenseStatus2ErrorBody]
] = _GetAccountLicenseStatus2Error()
