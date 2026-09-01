from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v1_result import FotaV1Result

ListUpgradesForSpecifiedStatusErrorBody: TypeAlias = FotaV1Result | RawError


@dataclass(frozen=True, slots=True)
class _ListUpgradesForSpecifiedStatusError:
    def map(self, response: HttpResponse) -> ListUpgradesForSpecifiedStatusErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV1Result](response)
            case _:
                return RawError(response)


list_upgrades_for_specified_status_error_mapper: Final[
    ErrorMapper[ListUpgradesForSpecifiedStatusErrorBody]
] = _ListUpgradesForSpecifiedStatusError()
