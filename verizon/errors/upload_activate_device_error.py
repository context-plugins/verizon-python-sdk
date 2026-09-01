from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UploadActivateDeviceErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UploadActivateDeviceError:
    def map(self, response: HttpResponse) -> UploadActivateDeviceErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


upload_activate_device_error_mapper: Final[ErrorMapper[UploadActivateDeviceErrorBody]] = _UploadActivateDeviceError()
