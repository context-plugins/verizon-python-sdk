from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.e_simrest_error_response import ESimrestErrorResponse

DeviceprovhistoryUsingPostErrorBody: TypeAlias = ESimrestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeviceprovhistoryUsingPostError:
    def map(self, response: HttpResponse) -> DeviceprovhistoryUsingPostErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[ESimrestErrorResponse](response)
            case _:
                return RawError(response)


deviceprovhistory_using_post_error_mapper: Final[
    ErrorMapper[DeviceprovhistoryUsingPostErrorBody]
] = _DeviceprovhistoryUsingPostError()
