from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

ListAccountDevicesErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _ListAccountDevicesError:
    def map(self, status_code: int, content: bytes) -> ListAccountDevicesErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV1Result](content)
            case _:
                return RawError(status_code, content)


list_account_devices_error_mapper: Final[ErrorMapper[ListAccountDevicesErrorBody]] = _ListAccountDevicesError()
