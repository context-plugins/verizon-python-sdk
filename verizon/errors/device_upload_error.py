from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

DeviceUploadErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeviceUploadError:
    def map(self, status_code: int, content: bytes) -> DeviceUploadErrorBody:
        match status_code:
            case 400:
                return decode_json[RestErrorResponse](content)
            case _:
                return RawError(status_code, content)


device_upload_error_mapper: Final[ErrorMapper[DeviceUploadErrorBody]] = _DeviceUploadError()
