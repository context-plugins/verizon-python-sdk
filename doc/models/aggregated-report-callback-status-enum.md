
# Aggregated Report Callback Status Enum

QUEUED or COMPLETED. Requests for IoT devices with cacheMode=0 (cached) have status=COMPLETED; all other requests are QUEUED.

## Enumeration

`AggregatedReportCallbackStatusEnum`

## Fields

| Name |
|  --- |
| `QUEUED` |
| `COMPLETED` |

## Example

```python
from verizon.models.aggregated_report_callback_status_enum import AggregatedReportCallbackStatusEnum

aggregated_report_callback_status = AggregatedReportCallbackStatusEnum.QUEUED
```

