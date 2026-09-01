from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

DeleteLocalProfileErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeleteLocalProfileError:
    def map(self, response: HttpResponse) -> DeleteLocalProfileErrorBody:
        match response.status_code:
            case 400:
                return decode_json[RestErrorResponse](response)
            case _:
                return RawError(response)


delete_local_profile_error_mapper: Final[ErrorMapper[DeleteLocalProfileErrorBody]] = _DeleteLocalProfileError()
