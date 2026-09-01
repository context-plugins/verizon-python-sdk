from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.mdm_error_response import MdmErrorResponse

DownloadMapmessagesErrorBody: TypeAlias = MdmErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DownloadMapmessagesError:
    def map(self, response: HttpResponse) -> DownloadMapmessagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 429 | 503:
                return decode_json[MdmErrorResponse](response)
            case _:
                return RawError(response)


download_mapmessages_error_mapper: Final[ErrorMapper[DownloadMapmessagesErrorBody]] = _DownloadMapmessagesError()
