from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

ScheduleFirmwareUpgradeErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _ScheduleFirmwareUpgradeError:
    def map(self, status_code: int, content: bytes) -> ScheduleFirmwareUpgradeErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


schedule_firmware_upgrade_error_mapper: Final[
    ErrorMapper[ScheduleFirmwareUpgradeErrorBody]
] = _ScheduleFirmwareUpgradeError()
