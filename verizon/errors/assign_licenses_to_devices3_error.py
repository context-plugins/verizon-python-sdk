from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

AssignLicensesToDevices3ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _AssignLicensesToDevices3Error:
    def map(self, status_code: int, content: bytes) -> AssignLicensesToDevices3ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


assign_licenses_to_devices3_error_mapper: Final[
    ErrorMapper[AssignLicensesToDevices3ErrorBody]
] = _AssignLicensesToDevices3Error()
