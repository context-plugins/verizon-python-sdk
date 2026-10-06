from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.response_error import ResponseError

GetConfigurationErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _GetConfigurationError:
    def map(self, status_code: int, content: bytes) -> GetConfigurationErrorBody:
        match status_code:
            case 403 | 404 | 429:
                return decode_json[ResponseError](content)
            case _:
                return RawError(status_code, content)


get_configuration_error_mapper: Final[ErrorMapper[GetConfigurationErrorBody]] = _GetConfigurationError()
