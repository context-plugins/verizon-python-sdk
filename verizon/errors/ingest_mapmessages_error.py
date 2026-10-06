from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.mdm_error_response import MdmErrorResponse

IngestMapmessagesErrorBody: TypeAlias = MdmErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _IngestMapmessagesError:
    def map(self, status_code: int, content: bytes) -> IngestMapmessagesErrorBody:
        match status_code:
            case 400 | 401 | 403 | 405 | 429 | 503:
                return decode_json[MdmErrorResponse](content)
            case _:
                return RawError(status_code, content)


ingest_mapmessages_error_mapper: Final[ErrorMapper[IngestMapmessagesErrorBody]] = _IngestMapmessagesError()
