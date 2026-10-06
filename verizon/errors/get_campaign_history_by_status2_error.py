from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetCampaignHistoryByStatus2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetCampaignHistoryByStatus2Error:
    def map(self, status_code: int, content: bytes) -> GetCampaignHistoryByStatus2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


get_campaign_history_by_status2_error_mapper: Final[
    ErrorMapper[GetCampaignHistoryByStatus2ErrorBody]
] = _GetCampaignHistoryByStatus2Error()
