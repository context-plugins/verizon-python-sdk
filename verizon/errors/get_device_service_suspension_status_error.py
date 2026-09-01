from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetDeviceServiceSuspensionStatusErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceServiceSuspensionStatusError:
    def map(self, response: HttpResponse) -> GetDeviceServiceSuspensionStatusErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


get_device_service_suspension_status_error_mapper: Final[
    ErrorMapper[GetDeviceServiceSuspensionStatusErrorBody]
] = _GetDeviceServiceSuspensionStatusError()
