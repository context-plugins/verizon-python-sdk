from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.response_error import ResponseError

DeleteConfigurationErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteConfigurationError:
    def map(self, response: HttpResponse) -> DeleteConfigurationErrorBody:
        match response.status_code:
            case 403 | 429:
                return decode_json[ResponseError](response)
            case _:
                return RawError(response)


delete_configuration_error_mapper: Final[ErrorMapper[DeleteConfigurationErrorBody]] = _DeleteConfigurationError()
