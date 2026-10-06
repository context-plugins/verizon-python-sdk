from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UsageSegmentationLabelAssociationErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UsageSegmentationLabelAssociationError:
    def map(self, status_code: int, content: bytes) -> UsageSegmentationLabelAssociationErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


usage_segmentation_label_association_error_mapper: Final[
    ErrorMapper[UsageSegmentationLabelAssociationErrorBody]
] = _UsageSegmentationLabelAssociationError()
