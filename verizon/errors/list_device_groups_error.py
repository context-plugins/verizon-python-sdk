from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListDeviceGroupsErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListDeviceGroupsError:
    def map(self, response: HttpResponse) -> ListDeviceGroupsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


list_device_groups_error_mapper: Final[ErrorMapper[ListDeviceGroupsErrorBody]] = _ListDeviceGroupsError()
