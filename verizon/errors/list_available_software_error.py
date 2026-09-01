from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ListAvailableSoftwareErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ListAvailableSoftwareError:
    def map(self, response: HttpResponse) -> ListAvailableSoftwareErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV2Result](response)
            case _:
                return RawError(response)


list_available_software_error_mapper: Final[ErrorMapper[ListAvailableSoftwareErrorBody]] = _ListAvailableSoftwareError()
