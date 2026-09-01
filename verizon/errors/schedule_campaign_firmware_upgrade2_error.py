from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

ScheduleCampaignFirmwareUpgrade2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _ScheduleCampaignFirmwareUpgrade2Error:
    def map(self, response: HttpResponse) -> ScheduleCampaignFirmwareUpgrade2ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[FotaV3Result](response)
            case _:
                return RawError(response)


schedule_campaign_firmware_upgrade2_error_mapper: Final[
    ErrorMapper[ScheduleCampaignFirmwareUpgrade2ErrorBody]
] = _ScheduleCampaignFirmwareUpgrade2Error()
