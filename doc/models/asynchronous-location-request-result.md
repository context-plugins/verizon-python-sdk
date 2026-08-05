
# Asynchronous Location Request Result

## Structure

`AsynchronousLocationRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | The transaction ID of the report. |
| `status` | [`ReportStatusEnum`](../../doc/models/report-status-enum.md) | Optional | Status of the report. |
| `estimated_duration` | `str` | Optional | Estimated number of minutes required to complete the report. |

## Example

```python
from verizon.models.asynchronous_location_request_result import AsynchronousLocationRequestResult
from verizon.models.report_status_enum import ReportStatusEnum

asynchronous_location_request_result = AsynchronousLocationRequestResult(
    txid='2017-12-11Te8b47da2-eeee-ffff-gggg-61815e1e97e9',
    status=ReportStatusEnum.INPROGRESS,
    estimated_duration='estimatedDuration2'
)
```

