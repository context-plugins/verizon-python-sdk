
# Bill Usage Request

Bill usage request.

## Structure

`BillUsageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier. |
| `start_date` | `str` | Required | Start date to search for billable usage, mm-dd-yyyy. |
| `end_date` | `str` | Required | End date to search for billable usage, mm-dd-yyyy. |
| `usage_for_all_accounts` | `bool` | Optional | Request usage for single or multiple accounts. |

## Example

```python
from verizon.models.bill_usage_request import BillUsageRequest

bill_usage_request = BillUsageRequest(
    account_name='1234567890-00001',
    start_date='04-01-2018',
    end_date='04-30-2018',
    usage_for_all_accounts=True
)
```

