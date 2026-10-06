from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

GetDeviceFirmwareUpgradeHistoryErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceFirmwareUpgradeHistoryError:
    def map(self, status_code: int, content: bytes) -> GetDeviceFirmwareUpgradeHistoryErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


get_device_firmware_upgrade_history_error_mapper: Final[
    ErrorMapper[GetDeviceFirmwareUpgradeHistoryErrorBody]
] = _GetDeviceFirmwareUpgradeHistoryError()
