from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.e_simrest_error_response import ESimrestErrorResponse

SetactivateUsingPostErrorBody: TypeAlias = ESimrestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _SetactivateUsingPostError:
    def map(self, status_code: int, content: bytes) -> SetactivateUsingPostErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 406 | 429:
                return decode_json[ESimrestErrorResponse](content)
            case _:
                return RawError(status_code, content)


setactivate_using_post_error_mapper: Final[ErrorMapper[SetactivateUsingPostErrorBody]] = _SetactivateUsingPostError()
