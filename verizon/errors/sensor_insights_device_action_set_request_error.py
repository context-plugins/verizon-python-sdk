from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.management_error400 import ManagementError400
from ..models.management_error403 import ManagementError403
from ..models.management_error404 import ManagementError404

SensorInsightsDeviceActionSetRequestErrorBody: TypeAlias = (
    ManagementError400 | ManagementError403 | ManagementError404 | RawError
)


@dataclass(frozen=True, slots=True)
class _SensorInsightsDeviceActionSetRequestError:
    def map(self, status_code: int, content: bytes) -> SensorInsightsDeviceActionSetRequestErrorBody:
        match status_code:
            case 400:
                return decode_json[ManagementError400](content)
            case 403:
                return decode_json[ManagementError403](content)
            case 404:
                return decode_json[ManagementError404](content)
            case _:
                return RawError(status_code, content)


sensor_insights_device_action_set_request_error_mapper: Final[
    ErrorMapper[SensorInsightsDeviceActionSetRequestErrorBody]
] = _SensorInsightsDeviceActionSetRequestError()
