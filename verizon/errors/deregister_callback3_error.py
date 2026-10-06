from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeregisterCallback3ErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeregisterCallback3Error:
    def map(self, status_code: int, content: bytes) -> DeregisterCallback3ErrorBody:
        match status_code:
            case 400:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


deregister_callback3_error_mapper: Final[ErrorMapper[DeregisterCallback3ErrorBody]] = _DeregisterCallback3Error()
