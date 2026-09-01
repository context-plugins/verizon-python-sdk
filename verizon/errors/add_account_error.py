from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

AddAccountErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _AddAccountError:
    def map(self, response: HttpResponse) -> AddAccountErrorBody:
        match response.status_code:
            case 400:
                return decode_json[DeviceLocationResult](response)
            case _:
                return RawError(response)


add_account_error_mapper: Final[ErrorMapper[AddAccountErrorBody]] = _AddAccountError()
