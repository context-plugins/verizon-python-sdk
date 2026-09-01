from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ActivateServiceForDevicesErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ActivateServiceForDevicesError:
    def map(self, response: HttpResponse) -> ActivateServiceForDevicesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


activate_service_for_devices_error_mapper: Final[
    ErrorMapper[ActivateServiceForDevicesErrorBody]
] = _ActivateServiceForDevicesError()
