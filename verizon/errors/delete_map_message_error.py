from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.mdm_error_response import MdmErrorResponse

DeleteMapMessageErrorBody: TypeAlias = MdmErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _DeleteMapMessageError:
    def map(self, response: HttpResponse) -> DeleteMapMessageErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 429 | 503:
                return decode_json[MdmErrorResponse](response)
            case _:
                return RawError(response)


delete_map_message_error_mapper: Final[ErrorMapper[DeleteMapMessageErrorBody]] = _DeleteMapMessageError()
