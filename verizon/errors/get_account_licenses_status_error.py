from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetAccountLicensesStatusErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountLicensesStatusError:
    def map(self, status_code: int, content: bytes) -> GetAccountLicensesStatusErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


get_account_licenses_status_error_mapper: Final[
    ErrorMapper[GetAccountLicensesStatusErrorBody]
] = _GetAccountLicensesStatusError()
