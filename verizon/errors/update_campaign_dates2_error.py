from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

UpdateCampaignDates2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _UpdateCampaignDates2Error:
    def map(self, response: HttpResponse) -> UpdateCampaignDates2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


update_campaign_dates2_error_mapper: Final[ErrorMapper[UpdateCampaignDates2ErrorBody]] = _UpdateCampaignDates2Error()
