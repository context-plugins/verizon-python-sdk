from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v2_result import FotaV2Result

ScheduleCampaignFirmwareUpgradeErrorBody: TypeAlias = FotaV2Result | RawError


@dataclass(frozen=True, slots=True)
class _ScheduleCampaignFirmwareUpgradeError:
    def map(self, status_code: int, content: bytes) -> ScheduleCampaignFirmwareUpgradeErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV2Result](content)
            case _:
                return RawError(status_code, content)


schedule_campaign_firmware_upgrade_error_mapper: Final[
    ErrorMapper[ScheduleCampaignFirmwareUpgradeErrorBody]
] = _ScheduleCampaignFirmwareUpgradeError()
