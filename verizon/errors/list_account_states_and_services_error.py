from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListAccountStatesAndServicesErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListAccountStatesAndServicesError:
    def map(self, response: HttpResponse) -> ListAccountStatesAndServicesErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


list_account_states_and_services_error_mapper: Final[
    ErrorMapper[ListAccountStatesAndServicesErrorBody]
] = _ListAccountStatesAndServicesError()
