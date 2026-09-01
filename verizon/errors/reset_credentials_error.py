from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_response import ErrorResponse

ResetCredentialsErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ResetCredentialsError:
    def map(self, response: HttpResponse) -> ResetCredentialsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


reset_credentials_error_mapper: Final[ErrorMapper[ResetCredentialsErrorBody]] = _ResetCredentialsError()
