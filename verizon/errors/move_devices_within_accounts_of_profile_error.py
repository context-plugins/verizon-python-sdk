from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

MoveDevicesWithinAccountsOfProfileErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _MoveDevicesWithinAccountsOfProfileError:
    def map(self, status_code: int, content: bytes) -> MoveDevicesWithinAccountsOfProfileErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


move_devices_within_accounts_of_profile_error_mapper: Final[
    ErrorMapper[MoveDevicesWithinAccountsOfProfileErrorBody]
] = _MoveDevicesWithinAccountsOfProfileError()
