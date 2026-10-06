from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

ScheduleCampaignFirmwareUpgrade2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _ScheduleCampaignFirmwareUpgrade2Error:
    def map(self, status_code: int, content: bytes) -> ScheduleCampaignFirmwareUpgrade2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


schedule_campaign_firmware_upgrade2_error_mapper: Final[
    ErrorMapper[ScheduleCampaignFirmwareUpgrade2ErrorBody]
] = _ScheduleCampaignFirmwareUpgrade2Error()
