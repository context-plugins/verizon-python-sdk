from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.device_location_result import DeviceLocationResult

CancelManagedAccountActionErrorBody: TypeAlias = DeviceLocationResult | RawError


@dataclass(frozen=True, slots=True)
class _CancelManagedAccountActionError:
    def map(self, status_code: int, content: bytes) -> CancelManagedAccountActionErrorBody:
        match status_code:
            case 400:
                return decode_json[DeviceLocationResult](content)
            case _:
                return RawError(status_code, content)


cancel_managed_account_action_error_mapper: Final[
    ErrorMapper[CancelManagedAccountActionErrorBody]
] = _CancelManagedAccountActionError()
