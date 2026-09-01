from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

RetrieveActiveMonitorsUsingPostErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveActiveMonitorsUsingPostError:
    def map(self, response: HttpResponse) -> RetrieveActiveMonitorsUsingPostErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


retrieve_active_monitors_using_post_error_mapper: Final[
    ErrorMapper[RetrieveActiveMonitorsUsingPostErrorBody]
] = _RetrieveActiveMonitorsUsingPostError()
