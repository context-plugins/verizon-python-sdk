
# Managed Account Cancel Response

## Structure

`ManagedAccountCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Required | Transaction identifier |
| `account_name` | `str` | Required | Managed account identifier |
| `paccount_name` | `str` | Required | Primary account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br><br>**Default**: `"Location"` |
| `status` | `str` | Required | Deactivate/cancel status, Success or Fail |
| `reason` | `str` | Required | Detailed reason |

## Example

```python
from verizon.models.managed_account_cancel_response import ManagedAccountCancelResponse
from verizon.models.service_name_enum import ServiceNameEnum

managed_account_cancel_response = ManagedAccountCancelResponse(
    txid='4fbff332-eeee-ffff-gggg-7e3bdc90bd28',
    account_name='1223334444-00001',
    paccount_name='1223334444-00001',
    service_name=ServiceNameEnum.LOCATION,
    status='Success',
    reason='Success'
)
```

