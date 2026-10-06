from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

DropCredentialsErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DropCredentialsError:
    def map(self, status_code: int, content: bytes) -> DropCredentialsErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


drop_credentials_error_mapper: Final[ErrorMapper[DropCredentialsErrorBody]] = _DropCredentialsError()
