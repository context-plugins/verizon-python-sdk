from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

CheckDevicesAvailabilityForActivationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _CheckDevicesAvailabilityForActivationError:
    def map(self, response: HttpResponse) -> CheckDevicesAvailabilityForActivationErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


check_devices_availability_for_activation_error_mapper: Final[
    ErrorMapper[CheckDevicesAvailabilityForActivationErrorBody]
] = _CheckDevicesAvailabilityForActivationError()
