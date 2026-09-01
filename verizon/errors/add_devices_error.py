from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

AddDevicesErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _AddDevicesError:
    def map(self, response: HttpResponse) -> AddDevicesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


add_devices_error_mapper: Final[ErrorMapper[AddDevicesErrorBody]] = _AddDevicesError()
