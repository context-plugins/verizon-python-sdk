from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ListDevicesWithLoggingEnabledErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ListDevicesWithLoggingEnabledError:
    def map(self, response: HttpResponse) -> ListDevicesWithLoggingEnabledErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


list_devices_with_logging_enabled_error_mapper: Final[
    ErrorMapper[ListDevicesWithLoggingEnabledErrorBody]
] = _ListDevicesWithLoggingEnabledError()
