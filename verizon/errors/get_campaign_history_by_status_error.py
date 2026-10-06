from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

GetCampaignHistoryByStatusErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _GetCampaignHistoryByStatusError:
    def map(self, status_code: int, content: bytes) -> GetCampaignHistoryByStatusErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV2Result](content)
            case _:
                return RawError(status_code, content)


get_campaign_history_by_status_error_mapper: Final[
    ErrorMapper[GetCampaignHistoryByStatusErrorBody]
] = _GetCampaignHistoryByStatusError()
