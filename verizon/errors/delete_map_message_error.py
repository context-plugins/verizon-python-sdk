from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.mdm_error_response import MdmErrorResponse

DeleteMapMessageErrorBody: TypeAlias = MdmErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeleteMapMessageError:
    def map(self, status_code: int, content: bytes) -> DeleteMapMessageErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 429 | 503:
                return decode_json[MdmErrorResponse](content)
            case _:
                return RawError(status_code, content)


delete_map_message_error_mapper: Final[ErrorMapper[DeleteMapMessageErrorBody]] = _DeleteMapMessageError()
