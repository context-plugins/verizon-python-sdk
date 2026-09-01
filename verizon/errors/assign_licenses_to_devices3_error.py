from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

AssignLicensesToDevices3ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _AssignLicensesToDevices3Error:
    def map(self, response: HttpResponse) -> AssignLicensesToDevices3ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


assign_licenses_to_devices3_error_mapper: Final[
    ErrorMapper[AssignLicensesToDevices3ErrorBody]
] = _AssignLicensesToDevices3Error()
