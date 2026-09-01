from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

BilledUsageInfoErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _BilledUsageInfoError:
    def map(self, response: HttpResponse) -> BilledUsageInfoErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


billed_usage_info_error_mapper: Final[ErrorMapper[BilledUsageInfoErrorBody]] = _BilledUsageInfoError()
