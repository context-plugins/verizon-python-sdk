
# Service Usage

## Structure

`ServiceUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier. |
| `transactions_count` | `str` | Optional | Total requests for the account during the reporting period. |

## Example

```python
from verizon.models.service_usage import ServiceUsage

service_usage = ServiceUsage(
    account_name='3333355555-00001',
    transactions_count='200'
)
```

