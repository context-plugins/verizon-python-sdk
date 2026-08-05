
# Synchronous Location Request Result

## Structure

`SynchronousLocationRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Required | The transaction ID of the report. |
| `status` | [`ReportStatusEnum`](../../doc/models/report-status-enum.md) | Required | Status of the report. |

## Example

```python
from verizon.models.report_status_enum import ReportStatusEnum
from verizon.models.synchronous_location_request_result import SynchronousLocationRequestResult

synchronous_location_request_result = SynchronousLocationRequestResult(
    txid='4be7c858-eeee-ffff-gggg-95061456d835',
    status=ReportStatusEnum.QUEUED
)
```

