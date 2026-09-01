from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListDevicesUsageHistoryErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListDevicesUsageHistoryError:
    def map(self, response: HttpResponse) -> ListDevicesUsageHistoryErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


list_devices_usage_history_error_mapper: Final[
    ErrorMapper[ListDevicesUsageHistoryErrorBody]
] = _ListDevicesUsageHistoryError()
