from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UpdateDevicesStateErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UpdateDevicesStateError:
    def map(self, response: HttpResponse) -> UpdateDevicesStateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


update_devices_state_error_mapper: Final[ErrorMapper[UpdateDevicesStateErrorBody]] = _UpdateDevicesStateError()
