from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

CancelCampaign2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _CancelCampaign2Error:
    def map(self, response: HttpResponse) -> CancelCampaign2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


cancel_campaign2_error_mapper: Final[ErrorMapper[CancelCampaign2ErrorBody]] = _CancelCampaign2Error()
