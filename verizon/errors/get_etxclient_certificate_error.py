from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

GetEtxclientCertificateErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _GetEtxclientCertificateError:
    def map(self, response: HttpResponse) -> GetEtxclientCertificateErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 404 | 429 | 500:
                return decode_json[EtxrespondingError](response)
            case _:
                return RawError(response)


get_etxclient_certificate_error_mapper: Final[
    ErrorMapper[GetEtxclientCertificateErrorBody]
] = _GetEtxclientCertificateError()
