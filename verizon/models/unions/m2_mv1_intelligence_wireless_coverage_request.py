from __future__ import annotations

from typing import TypeAlias

from ..get_wireless_coverage_request import GetWirelessCoverageRequest, GetWirelessCoverageRequestDict
from ..get_wireless_coverage_request_fwa import GetWirelessCoverageRequestFwa, GetWirelessCoverageRequestFwaDict

M2MV1IntelligenceWirelessCoverageRequest: TypeAlias = GetWirelessCoverageRequest | GetWirelessCoverageRequestFwa

M2MV1IntelligenceWirelessCoverageRequestDict: TypeAlias = (
    GetWirelessCoverageRequestDict | GetWirelessCoverageRequestFwaDict
)
