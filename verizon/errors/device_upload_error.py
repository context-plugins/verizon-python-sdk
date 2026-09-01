from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

DeviceUploadErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeviceUploadError:
    def map(self, response: HttpResponse) -> DeviceUploadErrorBody:
        match response.status_code:
            case 400:
                return decode_json[RestErrorResponse](response)
            case _:
                return RawError(response)


device_upload_error_mapper: Final[ErrorMapper[DeviceUploadErrorBody]] = _DeviceUploadError()
