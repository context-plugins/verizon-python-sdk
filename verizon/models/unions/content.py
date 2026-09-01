from __future__ import annotations

from typing import TypeAlias

from ..advisory_content import AdvisoryContent, AdvisoryContentDict
from ..exit_service_content import ExitServiceContent, ExitServiceContentDict
from ..generic_sign_content import GenericSignContent, GenericSignContentDict
from ..speed_limit_content import SpeedLimitContent, SpeedLimitContentDict
from ..work_zone_content import WorkZoneContent, WorkZoneContentDict

Content: TypeAlias = AdvisoryContent | WorkZoneContent | GenericSignContent | SpeedLimitContent | ExitServiceContent

ContentDict: TypeAlias = (
    AdvisoryContentDict | WorkZoneContentDict | GenericSignContentDict | SpeedLimitContentDict | ExitServiceContentDict
)
