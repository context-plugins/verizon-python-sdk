from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListDevicesInformationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListDevicesInformationError:
    def map(self, response: HttpResponse) -> ListDevicesInformationErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


list_devices_information_error_mapper: Final[
    ErrorMapper[ListDevicesInformationErrorBody]
] = _ListDevicesInformationError()
