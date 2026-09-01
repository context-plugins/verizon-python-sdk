from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UpdateDeviceIdErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UpdateDeviceIdError:
    def map(self, response: HttpResponse) -> UpdateDeviceIdErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


update_device_id_error_mapper: Final[ErrorMapper[UpdateDeviceIdErrorBody]] = _UpdateDeviceIdError()
