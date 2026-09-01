from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error_response import ErrorResponse

RetrieveCredentialsErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveCredentialsError:
    def map(self, response: HttpResponse) -> RetrieveCredentialsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case 401:
                return RawError(response)
            case _:
                return RawError(response)


retrieve_credentials_error_mapper: Final[ErrorMapper[RetrieveCredentialsErrorBody]] = _RetrieveCredentialsError()
