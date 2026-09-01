from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.e_simrest_error_response import ESimrestErrorResponse

NewactivatecodeErrorBody: TypeAlias = ESimrestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _NewactivatecodeError:
    def map(self, response: HttpResponse) -> NewactivatecodeErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[ESimrestErrorResponse](response)
            case _:
                return RawError(response)


newactivatecode_error_mapper: Final[ErrorMapper[NewactivatecodeErrorBody]] = _NewactivatecodeError()
