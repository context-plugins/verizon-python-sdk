from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

GetEtxclientCertificateErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _GetEtxclientCertificateError:
    def map(self, status_code: int, content: bytes) -> GetEtxclientCertificateErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 429 | 500:
                return decode_json[EtxrespondingError](content)
            case _:
                return RawError(status_code, content)


get_etxclient_certificate_error_mapper: Final[
    ErrorMapper[GetEtxclientCertificateErrorBody]
] = _GetEtxclientCertificateError()
