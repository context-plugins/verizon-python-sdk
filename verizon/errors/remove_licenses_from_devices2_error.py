from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

RemoveLicensesFromDevices2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _RemoveLicensesFromDevices2Error:
    def map(self, response: HttpResponse) -> RemoveLicensesFromDevices2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


remove_licenses_from_devices2_error_mapper: Final[
    ErrorMapper[RemoveLicensesFromDevices2ErrorBody]
] = _RemoveLicensesFromDevices2Error()
