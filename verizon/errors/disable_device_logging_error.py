from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

DisableDeviceLoggingErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _DisableDeviceLoggingError:
    def map(self, response: HttpResponse) -> DisableDeviceLoggingErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


disable_device_logging_error_mapper: Final[ErrorMapper[DisableDeviceLoggingErrorBody]] = _DisableDeviceLoggingError()
