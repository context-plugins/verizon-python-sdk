from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ChangeDevicesServicePlanErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ChangeDevicesServicePlanError:
    def map(self, response: HttpResponse) -> ChangeDevicesServicePlanErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


change_devices_service_plan_error_mapper: Final[
    ErrorMapper[ChangeDevicesServicePlanErrorBody]
] = _ChangeDevicesServicePlanError()
