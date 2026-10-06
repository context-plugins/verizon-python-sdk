from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

RemoveLicensesFromDevicesErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _RemoveLicensesFromDevicesError:
    def map(self, status_code: int, content: bytes) -> RemoveLicensesFromDevicesErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


remove_licenses_from_devices_error_mapper: Final[
    ErrorMapper[RemoveLicensesFromDevicesErrorBody]
] = _RemoveLicensesFromDevicesError()
