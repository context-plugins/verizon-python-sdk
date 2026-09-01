from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

DeregisterCallback3ErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeregisterCallback3Error:
    def map(self, response: HttpResponse) -> DeregisterCallback3ErrorBody:
        match response.status_code:
            case 400:
                return RawError(response)
            case _:
                return RawError(response)


deregister_callback3_error_mapper: Final[ErrorMapper[DeregisterCallback3ErrorBody]] = _DeregisterCallback3Error()
