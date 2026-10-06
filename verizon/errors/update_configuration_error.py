from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.response_error import ResponseError

UpdateConfigurationErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _UpdateConfigurationError:
    def map(self, status_code: int, content: bytes) -> UpdateConfigurationErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429:
                return decode_json[ResponseError](content)
            case _:
                return RawError(status_code, content)


update_configuration_error_mapper: Final[ErrorMapper[UpdateConfigurationErrorBody]] = _UpdateConfigurationError()
