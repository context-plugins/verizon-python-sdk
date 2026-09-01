from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ResetConnectivityManagementPasswordErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ResetConnectivityManagementPasswordError:
    def map(self, response: HttpResponse) -> ResetConnectivityManagementPasswordErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


reset_connectivity_management_password_error_mapper: Final[
    ErrorMapper[ResetConnectivityManagementPasswordErrorBody]
] = _ResetConnectivityManagementPasswordError()
