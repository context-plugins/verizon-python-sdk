from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UsageSegmentationLabelDeletionErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UsageSegmentationLabelDeletionError:
    def map(self, status_code: int, content: bytes) -> UsageSegmentationLabelDeletionErrorBody:
        match status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](content)
            case _:
                return RawError(status_code, content)


usage_segmentation_label_deletion_error_mapper: Final[
    ErrorMapper[UsageSegmentationLabelDeletionErrorBody]
] = _UsageSegmentationLabelDeletionError()
