from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

DeviceUploadStatusErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _DeviceUploadStatusError:
    def map(self, status_code: int, content: bytes) -> DeviceUploadStatusErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


device_upload_status_error_mapper: Final[ErrorMapper[DeviceUploadStatusErrorBody]] = _DeviceUploadStatusError()
