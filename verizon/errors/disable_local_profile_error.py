from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

DisableLocalProfileErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DisableLocalProfileError:
    def map(self, response: HttpResponse) -> DisableLocalProfileErrorBody:
        match response.status_code:
            case 400:
                return decode_json[RestErrorResponse](response)
            case _:
                return RawError(response)


disable_local_profile_error_mapper: Final[ErrorMapper[DisableLocalProfileErrorBody]] = _DisableLocalProfileError()
