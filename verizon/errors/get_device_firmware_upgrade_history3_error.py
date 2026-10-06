from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetDeviceFirmwareUpgradeHistory3ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceFirmwareUpgradeHistory3Error:
    def map(self, status_code: int, content: bytes) -> GetDeviceFirmwareUpgradeHistory3ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


get_device_firmware_upgrade_history3_error_mapper: Final[
    ErrorMapper[GetDeviceFirmwareUpgradeHistory3ErrorBody]
] = _GetDeviceFirmwareUpgradeHistory3Error()
