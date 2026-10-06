from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetDeviceServiceSuspensionStatusErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetDeviceServiceSuspensionStatusError:
    def map(self, status_code: int, content: bytes) -> GetDeviceServiceSuspensionStatusErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


get_device_service_suspension_status_error_mapper: Final[
    ErrorMapper[GetDeviceServiceSuspensionStatusErrorBody]
] = _GetDeviceServiceSuspensionStatusError()
