from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

EndConnectivityManagementSessionErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _EndConnectivityManagementSessionError:
    def map(self, response: HttpResponse) -> EndConnectivityManagementSessionErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


end_connectivity_management_session_error_mapper: Final[
    ErrorMapper[EndConnectivityManagementSessionErrorBody]
] = _EndConnectivityManagementSessionError()
