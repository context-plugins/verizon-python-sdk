
# Location Report Status

Status of the report.

## Structure

`LocationReportStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | The transaction ID of the report. |
| `status` | [`ReportStatusEnum`](../../doc/models/report-status-enum.md) | Optional | Status of the report. |

## Example

```python
from verizon.models.location_report_status import LocationReportStatus
from verizon.models.report_status_enum import ReportStatusEnum

location_report_status = LocationReportStatus(
    txid='2c90bd28-eeee-ffff-gggg-7e3bd4fbff33',
    status=ReportStatusEnum.QUEUED
)
```

