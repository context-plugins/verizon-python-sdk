from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

StartQueuedSmsdeliveryErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _StartQueuedSmsdeliveryError:
    def map(self, response: HttpResponse) -> StartQueuedSmsdeliveryErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


start_queued_smsdelivery_error_mapper: Final[
    ErrorMapper[StartQueuedSmsdeliveryErrorBody]
] = _StartQueuedSmsdeliveryError()
