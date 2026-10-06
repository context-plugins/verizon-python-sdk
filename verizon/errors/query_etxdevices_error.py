from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

QueryEtxdevicesErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _QueryEtxdevicesError:
    def map(self, status_code: int, content: bytes) -> QueryEtxdevicesErrorBody:
        match status_code:
            case 400 | 401 | 500:
                return decode_json[EtxrespondingError](content)
            case _:
                return RawError(status_code, content)


query_etxdevices_error_mapper: Final[ErrorMapper[QueryEtxdevicesErrorBody]] = _QueryEtxdevicesError()
