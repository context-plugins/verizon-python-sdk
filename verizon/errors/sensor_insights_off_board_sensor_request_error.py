from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.management_error import ManagementError
from ..models.management_error400 import ManagementError400
from ..models.management_error403 import ManagementError403

SensorInsightsOffBoardSensorRequestErrorBody: TypeAlias = (
    ManagementError400 | ManagementError | ManagementError403 | RawError
)


@dataclass(frozen=True, slots=True)
class _SensorInsightsOffBoardSensorRequestError:
    def map(self, response: HttpResponse) -> SensorInsightsOffBoardSensorRequestErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ManagementError400](response)
            case 401:
                return decode_json[ManagementError](response)
            case 403:
                return decode_json[ManagementError403](response)
            case _:
                return RawError(response)


sensor_insights_off_board_sensor_request_error_mapper: Final[
    ErrorMapper[SensorInsightsOffBoardSensorRequestErrorBody]
] = _SensorInsightsOffBoardSensorRequestError()
