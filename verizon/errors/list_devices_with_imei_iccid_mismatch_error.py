from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListDevicesWithImeiIccidMismatchErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListDevicesWithImeiIccidMismatchError:
    def map(self, response: HttpResponse) -> ListDevicesWithImeiIccidMismatchErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


list_devices_with_imei_iccid_mismatch_error_mapper: Final[
    ErrorMapper[ListDevicesWithImeiIccidMismatchErrorBody]
] = _ListDevicesWithImeiIccidMismatchError()
