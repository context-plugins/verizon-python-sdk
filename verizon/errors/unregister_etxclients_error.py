from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.etxresponding_error import EtxrespondingError

UnregisterEtxclientsErrorBody: TypeAlias = EtxrespondingError | RawError


@dataclass(frozen=True, slots=True)
class _UnregisterEtxclientsError:
    def map(self, status_code: int, content: bytes) -> UnregisterEtxclientsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 503:
                return decode_json[EtxrespondingError](content)
            case _:
                return RawError(status_code, content)


unregister_etxclients_error_mapper: Final[ErrorMapper[UnregisterEtxclientsErrorBody]] = _UnregisterEtxclientsError()
