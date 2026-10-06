from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

BilledUsageInfoErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _BilledUsageInfoError:
    def map(self, status_code: int, content: bytes) -> BilledUsageInfoErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


billed_usage_info_error_mapper: Final[ErrorMapper[BilledUsageInfoErrorBody]] = _BilledUsageInfoError()
