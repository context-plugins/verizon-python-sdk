from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

GetAccountInformationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountInformationError:
    def map(self, response: HttpResponse) -> GetAccountInformationErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


get_account_information_error_mapper: Final[ErrorMapper[GetAccountInformationErrorBody]] = _GetAccountInformationError()
