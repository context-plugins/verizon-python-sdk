from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.security_result import SecurityResult

AssignLicenseToDevicesErrorBody: TypeAlias = SecurityResult | RawError


@dataclass(frozen=True, slots=True)
class _AssignLicenseToDevicesError:
    def map(self, response: HttpResponse) -> AssignLicenseToDevicesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[SecurityResult](response)
            case _:
                return RawError(response)


assign_license_to_devices_error_mapper: Final[
    ErrorMapper[AssignLicenseToDevicesErrorBody]
] = _AssignLicenseToDevicesError()
