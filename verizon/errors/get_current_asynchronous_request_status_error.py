from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetCurrentAsynchronousRequestStatusErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetCurrentAsynchronousRequestStatusError:
    def map(self, response: HttpResponse) -> GetCurrentAsynchronousRequestStatusErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


get_current_asynchronous_request_status_error_mapper: Final[
    ErrorMapper[GetCurrentAsynchronousRequestStatusErrorBody]
] = _GetCurrentAsynchronousRequestStatusError()
