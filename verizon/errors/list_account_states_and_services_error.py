from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListAccountStatesAndServicesErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListAccountStatesAndServicesError:
    def map(self, status_code: int, content: bytes) -> ListAccountStatesAndServicesErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


list_account_states_and_services_error_mapper: Final[
    ErrorMapper[ListAccountStatesAndServicesErrorBody]
] = _ListAccountStatesAndServicesError()
