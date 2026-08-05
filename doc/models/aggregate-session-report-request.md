
# Aggregate Session Report Request

Request for getting an aggregated session report.

## Structure

`AggregateSessionReportRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |
| `start_date` | `str` | Optional | Start date of session to include. If not specified  information will be shown from the earliest available (180 days). Can be either date in ISO 8601 format or predefined constants. |
| `end_date` | `str` | Optional | End date of session to include. If not specified  information will be shown to the latest available. Can be either date in ISO 8601 format or predefined constants. |
| `imei` | `List[str]` | Required | Devices for which return usage info. Could be 0, 1 or more. In case of 0 will return all devices belonging to customer (except of filtered by other parameters). |
| `device_group` | `str` | Optional | Optional filter — only include devices matching this device group name. |
| `data_plan` | `str` | Optional | Optional filter — only include devices matching this carrier rate plan code. |
| `no_session_flag` | `bool` | Optional | Optional filter — when "true", returns only devices with no sessions. |

## Example

```python
from verizon.models.aggregate_session_report_request import AggregateSessionReportRequest

aggregate_session_report_request = AggregateSessionReportRequest(
    account_number='0000123456-00001',
    imei=[
        '15-digit IMEI'
    ],
    start_date='2022-12-09T22:01:06.217Z',
    end_date='2022-12-09T22:01:08.734Z',
    device_group='string',
    data_plan='string',
    no_session_flag=False
)
```

