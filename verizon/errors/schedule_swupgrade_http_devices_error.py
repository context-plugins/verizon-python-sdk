from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ScheduleSwupgradeHttpDevicesErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ScheduleSwupgradeHttpDevicesError:
    def map(self, status_code: int, content: bytes) -> ScheduleSwupgradeHttpDevicesErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV2Result](content)
            case _:
                return RawError(status_code, content)


schedule_swupgrade_http_devices_error_mapper: Final[
    ErrorMapper[ScheduleSwupgradeHttpDevicesErrorBody]
] = _ScheduleSwupgradeHttpDevicesError()
