from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetCampaignInformation2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetCampaignInformation2Error:
    def map(self, response: HttpResponse) -> GetCampaignInformation2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


get_campaign_information2_error_mapper: Final[
    ErrorMapper[GetCampaignInformation2ErrorBody]
] = _GetCampaignInformation2Error()
