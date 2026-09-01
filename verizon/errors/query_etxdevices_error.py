from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

QueryEtxdevicesErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _QueryEtxdevicesError:
    def map(self, response: HttpResponse) -> QueryEtxdevicesErrorBody:
        match response.status_code:
            case 400 | 401 | 500:
                return decode_json[EtxrespondingError](response)
            case _:
                return RawError(response)


query_etxdevices_error_mapper: Final[ErrorMapper[QueryEtxdevicesErrorBody]] = _QueryEtxdevicesError()
