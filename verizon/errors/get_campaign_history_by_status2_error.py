from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetCampaignHistoryByStatus2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetCampaignHistoryByStatus2Error:
    def map(self, response: HttpResponse) -> GetCampaignHistoryByStatus2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


get_campaign_history_by_status2_error_mapper: Final[
    ErrorMapper[GetCampaignHistoryByStatus2ErrorBody]
] = _GetCampaignHistoryByStatus2Error()
