from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.management_error import ManagementError
from ..models.management_error400 import ManagementError400
from ..models.management_error403 import ManagementError403
from ..models.management_error404 import ManagementError404

SensorInsightsDeleteNotificationGroupErrorBody: TypeAlias = (
    ManagementError400 | ManagementError | ManagementError403 | ManagementError404 | RawError
)


@dataclass(frozen=True, slots=True)
class _SensorInsightsDeleteNotificationGroupError:
    def map(self, response: HttpResponse) -> SensorInsightsDeleteNotificationGroupErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ManagementError400](response)
            case 401:
                return decode_json[ManagementError](response)
            case 403:
                return decode_json[ManagementError403](response)
            case 404:
                return decode_json[ManagementError404](response)
            case _:
                return RawError(response)


sensor_insights_delete_notification_group_error_mapper: Final[
    ErrorMapper[SensorInsightsDeleteNotificationGroupErrorBody]
] = _SensorInsightsDeleteNotificationGroupError()
