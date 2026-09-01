from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.rest_error_response import RestErrorResponse

ProfileToActivateDeviceErrorBody: TypeAlias = RestErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ProfileToActivateDeviceError:
    def map(self, response: HttpResponse) -> ProfileToActivateDeviceErrorBody:
        match response.status_code:
            case 400:
                return decode_json[RestErrorResponse](response)
            case _:
                return RawError(response)


profile_to_activate_device_error_mapper: Final[
    ErrorMapper[ProfileToActivateDeviceErrorBody]
] = _ProfileToActivateDeviceError()
