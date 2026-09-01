from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ListAccountDevices2ErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ListAccountDevices2Error:
    def map(self, response: HttpResponse) -> ListAccountDevices2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


list_account_devices2_error_mapper: Final[ErrorMapper[ListAccountDevices2ErrorBody]] = _ListAccountDevices2Error()
