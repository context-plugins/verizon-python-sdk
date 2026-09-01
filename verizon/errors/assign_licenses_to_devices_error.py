from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

AssignLicensesToDevicesErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _AssignLicensesToDevicesError:
    def map(self, response: HttpResponse) -> AssignLicensesToDevicesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV1Result](response)
            case _:
                return RawError(response)


assign_licenses_to_devices_error_mapper: Final[
    ErrorMapper[AssignLicensesToDevicesErrorBody]
] = _AssignLicensesToDevicesError()
