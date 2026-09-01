from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

CreateDeviceGroupErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _CreateDeviceGroupError:
    def map(self, response: HttpResponse) -> CreateDeviceGroupErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


create_device_group_error_mapper: Final[ErrorMapper[CreateDeviceGroupErrorBody]] = _CreateDeviceGroupError()
