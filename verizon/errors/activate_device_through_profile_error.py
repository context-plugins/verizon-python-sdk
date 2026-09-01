from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

ActivateDeviceThroughProfileErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ActivateDeviceThroughProfileError:
    def map(self, response: HttpResponse) -> ActivateDeviceThroughProfileErrorBody:
        match response.status_code:
            case 400:
                return decode_json[RestErrorResponse](response)
            case _:
                return RawError(response)


activate_device_through_profile_error_mapper: Final[
    ErrorMapper[ActivateDeviceThroughProfileErrorBody]
] = _ActivateDeviceThroughProfileError()
