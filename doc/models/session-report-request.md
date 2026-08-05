
# Session Report Request

Request for obtaining a session report.

## Structure

`SessionReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |
| `imei` | `str` | Required | The International Mobile Equipment Identifier of the device. |
| `start_date` | `str` | Optional | Start date of session to include. If not specified  information will be shown from the earliest available (180 days). Can be either date in ISO 8601 format or predefined constants. |
| `end_date` | `str` | Optional | End date of session to include. If not specified  information will be shown to the latest available. Can be either date in ISO 8601 format or predefined constants. |
| `duration_low` | `int` | Optional | Optional filter — minimum session duration |
| `duration_high` | `int` | Optional | Optional filter — maximum session duration |

## Example

```python
from verizon.models.session_report_request import SessionReportRequest

session_report_request = SessionReportRequest(
    account_number='0000123456-00001',
    imei='15-digit IMEI',
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    duration_low=0,
    duration_high=0
)
```

