from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.e_simrest_error_response import ESimrestErrorResponse

NewactivatecodeErrorBody: TypeAlias = ESimrestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _NewactivatecodeError:
    def map(self, status_code: int, content: bytes) -> NewactivatecodeErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[ESimrestErrorResponse](content)
            case _:
                return RawError(status_code, content)


newactivatecode_error_mapper: Final[ErrorMapper[NewactivatecodeErrorBody]] = _NewactivatecodeError()
