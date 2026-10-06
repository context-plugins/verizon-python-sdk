from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

GetEtxconnectionUrlMultiMecErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _GetEtxconnectionUrlMultiMecError:
    def map(self, status_code: int, content: bytes) -> GetEtxconnectionUrlMultiMecErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 503:
                return decode_json[EtxrespondingError](content)
            case _:
                return RawError(status_code, content)


get_etxconnection_url_multi_mec_error_mapper: Final[
    ErrorMapper[GetEtxconnectionUrlMultiMecErrorBody]
] = _GetEtxconnectionUrlMultiMecError()
