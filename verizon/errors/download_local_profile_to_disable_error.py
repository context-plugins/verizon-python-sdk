from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

DownloadLocalProfileToDisableErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _DownloadLocalProfileToDisableError:
    def map(self, response: HttpResponse) -> DownloadLocalProfileToDisableErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


download_local_profile_to_disable_error_mapper: Final[
    ErrorMapper[DownloadLocalProfileToDisableErrorBody]
] = _DownloadLocalProfileToDisableError()
