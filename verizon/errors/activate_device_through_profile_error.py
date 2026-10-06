from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

ActivateDeviceThroughProfileErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ActivateDeviceThroughProfileError:
    def map(self, status_code: int, content: bytes) -> ActivateDeviceThroughProfileErrorBody:
        match status_code:
            case 400:
                return decode_json[RestErrorResponse](content)
            case _:
                return RawError(status_code, content)


activate_device_through_profile_error_mapper: Final[
    ErrorMapper[ActivateDeviceThroughProfileErrorBody]
] = _ActivateDeviceThroughProfileError()
