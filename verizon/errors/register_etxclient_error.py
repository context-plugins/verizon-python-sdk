from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

RegisterEtxclientErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _RegisterEtxclientError:
    def map(self, response: HttpResponse) -> RegisterEtxclientErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 429 | 503:
                return decode_json[EtxrespondingError](response)
            case _:
                return RawError(response)


register_etxclient_error_mapper: Final[ErrorMapper[RegisterEtxclientErrorBody]] = _RegisterEtxclientError()
