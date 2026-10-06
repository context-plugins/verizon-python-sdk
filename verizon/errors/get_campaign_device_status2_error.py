from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.fota_v3_result import FotaV3Result

GetCampaignDeviceStatus2ErrorBody: TypeAlias = FotaV3Result | RawError


@dataclass(frozen=True, slots=True)
class _GetCampaignDeviceStatus2Error:
    def map(self, status_code: int, content: bytes) -> GetCampaignDeviceStatus2ErrorBody:
        match status_code:
            case 400:
                return decode_json[FotaV3Result](content)
            case _:
                return RawError(status_code, content)


get_campaign_device_status2_error_mapper: Final[
    ErrorMapper[GetCampaignDeviceStatus2ErrorBody]
] = _GetCampaignDeviceStatus2Error()
