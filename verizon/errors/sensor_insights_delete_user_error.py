from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.management_error import ManagementError
from ..models.management_error400 import ManagementError400
from ..models.management_error403 import ManagementError403
from ..models.management_error404 import ManagementError404

SensorInsightsDeleteUserErrorBody: TypeAlias = (
    ManagementError400 | ManagementError | ManagementError403 | ManagementError404 | RawError
)


@dataclass(frozen=True, slots=True)
class _SensorInsightsDeleteUserError:
    def map(self, status_code: int, content: bytes) -> SensorInsightsDeleteUserErrorBody:
        match status_code:
            case 400:
                return decode_json[ManagementError400](content)
            case 401:
                return decode_json[ManagementError](content)
            case 403:
                return decode_json[ManagementError403](content)
            case 404:
                return decode_json[ManagementError404](content)
            case _:
                return RawError(status_code, content)


sensor_insights_delete_user_error_mapper: Final[
    ErrorMapper[SensorInsightsDeleteUserErrorBody]
] = _SensorInsightsDeleteUserError()
