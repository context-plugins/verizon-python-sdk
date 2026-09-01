from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

UnregisterEtxclientsErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _UnregisterEtxclientsError:
    def map(self, response: HttpResponse) -> UnregisterEtxclientsErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 429 | 503:
                return decode_json[EtxrespondingError](response)
            case _:
                return RawError(response)


unregister_etxclients_error_mapper: Final[ErrorMapper[UnregisterEtxclientsErrorBody]] = _UnregisterEtxclientsError()
