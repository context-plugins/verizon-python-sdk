from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

RenewEtxclientCertificateErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _RenewEtxclientCertificateError:
    def map(self, response: HttpResponse) -> RenewEtxclientCertificateErrorBody:
        match response.status_code:
            case 400 | 401 | 403 | 429 | 503:
                return decode_json[EtxrespondingError](response)
            case _:
                return RawError(response)


renew_etxclient_certificate_error_mapper: Final[
    ErrorMapper[RenewEtxclientCertificateErrorBody]
] = _RenewEtxclientCertificateError()
