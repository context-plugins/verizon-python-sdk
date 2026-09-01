from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.response_error import ResponseError

UpdateConfigurationErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateConfigurationError:
    def map(self, response: HttpResponse) -> UpdateConfigurationErrorBody:
        match response.status_code:
            case 400 | 403 | 404 | 429:
                return decode_json[ResponseError](response)
            case _:
                return RawError(response)


update_configuration_error_mapper: Final[ErrorMapper[UpdateConfigurationErrorBody]] = _UpdateConfigurationError()
