from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_response import ErrorResponse

GenerateCredentialsErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _GenerateCredentialsError:
    def map(self, response: HttpResponse) -> GenerateCredentialsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


generate_credentials_error_mapper: Final[ErrorMapper[GenerateCredentialsErrorBody]] = _GenerateCredentialsError()
