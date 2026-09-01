from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

RemoveLicensesFromDevices3ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _RemoveLicensesFromDevices3Error:
    def map(self, response: HttpResponse) -> RemoveLicensesFromDevices3ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


remove_licenses_from_devices3_error_mapper: Final[
    ErrorMapper[RemoveLicensesFromDevices3ErrorBody]
] = _RemoveLicensesFromDevices3Error()
