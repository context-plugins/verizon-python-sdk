from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

DownloadLocalProfileToDisableErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _DownloadLocalProfileToDisableError:
    def map(self, status_code: int, content: bytes) -> DownloadLocalProfileToDisableErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


download_local_profile_to_disable_error_mapper: Final[
    ErrorMapper[DownloadLocalProfileToDisableErrorBody]
] = _DownloadLocalProfileToDisableError()
