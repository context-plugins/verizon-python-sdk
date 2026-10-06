from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

SynchronizeDeviceFirmwareErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _SynchronizeDeviceFirmwareError:
    def map(self, status_code: int, content: bytes) -> SynchronizeDeviceFirmwareErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


synchronize_device_firmware_error_mapper: Final[
    ErrorMapper[SynchronizeDeviceFirmwareErrorBody]
] = _SynchronizeDeviceFirmwareError()
