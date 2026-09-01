from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

ListAccountServicePlansErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _ListAccountServicePlansError:
    def map(self, response: HttpResponse) -> ListAccountServicePlansErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


list_account_service_plans_error_mapper: Final[
    ErrorMapper[ListAccountServicePlansErrorBody]
] = _ListAccountServicePlansError()
