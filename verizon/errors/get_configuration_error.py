from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.response_error import ResponseError

GetConfigurationErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _GetConfigurationError:
    def map(self, response: HttpResponse) -> GetConfigurationErrorBody:
        match response.status_code:
            case 403 | 404 | 429:
                return decode_json[ResponseError](response)
            case _:
                return RawError(response)


get_configuration_error_mapper: Final[ErrorMapper[GetConfigurationErrorBody]] = _GetConfigurationError()
