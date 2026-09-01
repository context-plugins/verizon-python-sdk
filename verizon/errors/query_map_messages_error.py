from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.mdm_error_response import MdmErrorResponse

QueryMapMessagesErrorBody: TypeAlias = MdmErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _QueryMapMessagesError:
    def map(self, response: HttpResponse) -> QueryMapMessagesErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 405 | 429 | 503:
                return decode_json[MdmErrorResponse](response)
            case _:
                return RawError(response)


query_map_messages_error_mapper: Final[ErrorMapper[QueryMapMessagesErrorBody]] = _QueryMapMessagesError()
