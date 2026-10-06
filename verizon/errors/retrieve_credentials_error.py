from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

RetrieveCredentialsErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveCredentialsError:
    def map(self, status_code: int, content: bytes) -> RetrieveCredentialsErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case 401:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


retrieve_credentials_error_mapper: Final[ErrorMapper[RetrieveCredentialsErrorBody]] = _RetrieveCredentialsError()
