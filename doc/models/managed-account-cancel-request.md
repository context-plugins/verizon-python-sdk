
# Managed Account Cancel Request

## Structure

`ManagedAccountCancelRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Managed account identifier |
| `paccount_name` | `str` | Required | Primary Account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br><br>**Default**: `"Location"` |
| `mtype` | `str` | Required | SKU name |
| `txid` | `str` | Required | Transaction identifier returned by provision request |

## Example

```python
from verizon.models.managed_account_cancel_request import ManagedAccountCancelRequest
from verizon.models.service_name_enum import ServiceNameEnum

managed_account_cancel_request = ManagedAccountCancelRequest(
    account_name='1223334444-00001',
    paccount_name='1223334444-00001',
    service_name=ServiceNameEnum.LOCATION,
    mtype='TS-LOC-COARSE-CellID-5K',
    txid='d4fbff33-eeee-ffff-gggg-2c90bd287e3b'
)
```

