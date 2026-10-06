from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.management_error import ManagementError

SensorInsightsListDevicesRequestErrorBody: TypeAlias = ManagementError | RawError


@dataclass(frozen=True, slots=True)
class _SensorInsightsListDevicesRequestError:
    def map(self, status_code: int, content: bytes) -> SensorInsightsListDevicesRequestErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 406 | 415 | 429 | 500:
                return decode_json[ManagementError](content)
            case _:
                return RawError(status_code, content)


sensor_insights_list_devices_request_error_mapper: Final[
    ErrorMapper[SensorInsightsListDevicesRequestErrorBody]
] = _SensorInsightsListDevicesRequestError()
