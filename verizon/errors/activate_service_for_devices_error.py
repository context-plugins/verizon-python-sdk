from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ActivateServiceForDevicesErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ActivateServiceForDevicesError:
    def map(self, status_code: int, content: bytes) -> ActivateServiceForDevicesErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


activate_service_for_devices_error_mapper: Final[
    ErrorMapper[ActivateServiceForDevicesErrorBody]
] = _ActivateServiceForDevicesError()
