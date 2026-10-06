from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.response_error import ResponseError

DeleteConfigurationErrorBody: TypeAlias = ResponseError | RawError


@dataclass(frozen=True, slots=True)
class _DeleteConfigurationError:
    def map(self, status_code: int, content: bytes) -> DeleteConfigurationErrorBody:
        match status_code:
            case 403 | 429:
                return decode_json[ResponseError](content)
            case _:
                return RawError(status_code, content)


delete_configuration_error_mapper: Final[ErrorMapper[DeleteConfigurationErrorBody]] = _DeleteConfigurationError()
