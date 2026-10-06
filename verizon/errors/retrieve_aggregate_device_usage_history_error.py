from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

RetrieveAggregateDeviceUsageHistoryErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveAggregateDeviceUsageHistoryError:
    def map(self, status_code: int, content: bytes) -> RetrieveAggregateDeviceUsageHistoryErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


retrieve_aggregate_device_usage_history_error_mapper: Final[
    ErrorMapper[RetrieveAggregateDeviceUsageHistoryErrorBody]
] = _RetrieveAggregateDeviceUsageHistoryError()
