from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

ListRegisteredCallbacks2ErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _ListRegisteredCallbacks2Error:
    def map(self, response: HttpResponse) -> ListRegisteredCallbacks2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceLocationResult](response)
            case _:
                return RawError(response)


list_registered_callbacks2_error_mapper: Final[
    ErrorMapper[ListRegisteredCallbacks2ErrorBody]
] = _ListRegisteredCallbacks2Error()
