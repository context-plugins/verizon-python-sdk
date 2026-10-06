from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

GetEtxconnectionUrlErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _GetEtxconnectionUrlError:
    def map(self, status_code: int, content: bytes) -> GetEtxconnectionUrlErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 503:
                return decode_json[EtxrespondingError](content)
            case _:
                return RawError(status_code, content)


get_etxconnection_url_error_mapper: Final[ErrorMapper[GetEtxconnectionUrlErrorBody]] = _GetEtxconnectionUrlError()
