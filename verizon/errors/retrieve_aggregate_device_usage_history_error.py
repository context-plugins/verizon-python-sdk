from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

RetrieveAggregateDeviceUsageHistoryErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveAggregateDeviceUsageHistoryError:
    def map(self, response: HttpResponse) -> RetrieveAggregateDeviceUsageHistoryErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


retrieve_aggregate_device_usage_history_error_mapper: Final[
    ErrorMapper[RetrieveAggregateDeviceUsageHistoryErrorBody]
] = _RetrieveAggregateDeviceUsageHistoryError()
