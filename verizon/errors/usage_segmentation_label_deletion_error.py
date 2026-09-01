from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.connectivity_management_result import ConnectivityManagementResult

UsageSegmentationLabelDeletionErrorBody: TypeAlias = ConnectivityManagementResult | RawError


@dataclass(frozen=True, slots=True)
class _UsageSegmentationLabelDeletionError:
    def map(self, response: HttpResponse) -> UsageSegmentationLabelDeletionErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ConnectivityManagementResult](response)
            case _:
                return RawError(response)


usage_segmentation_label_deletion_error_mapper: Final[
    ErrorMapper[UsageSegmentationLabelDeletionErrorBody]
] = _UsageSegmentationLabelDeletionError()
