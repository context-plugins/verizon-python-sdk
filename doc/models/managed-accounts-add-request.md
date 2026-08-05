
# Managed Accounts Add Request

## Structure

`ManagedAccountsAddRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account identifier |
| `service_name` | [`ServiceNameEnum`](../../doc/models/service-name-enum.md) | Required | Service name<br><br>**Default**: `"Location"` |
| `mtype` | `str` | Required | SKU name |
| `managed_acc_list` | `List[str]` | Required | managed account list |

## Example

```python
from verizon.models.managed_accounts_add_request import ManagedAccountsAddRequest
from verizon.models.service_name_enum import ServiceNameEnum

managed_accounts_add_request = ManagedAccountsAddRequest(
    account_name='1234567890-00001',
    service_name=ServiceNameEnum.LOCATION,
    mtype='TS-LOC-COARSE-CellID-Aggr',
    managed_acc_list=[
        '1223334444-00001',
        '2334445555-00001',
        '3445556666-00001'
    ]
)
```

