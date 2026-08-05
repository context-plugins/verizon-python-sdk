
# Managed Accounts Add Response

## Structure

`ManagedAccountsAddResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tx_id` | `str` | Optional | Transaction identifier |
| `status_list` | [`List[StatusList]`](../../doc/models/status-list.md) | Optional | - |

## Example

```python
from verizon.models.managed_accounts_add_response import ManagedAccountsAddResponse
from verizon.models.status_list import StatusList

managed_accounts_add_response = ManagedAccountsAddResponse(
    tx_id='2c90bd28-eeee-ffff-gggg-7e3bd4fbff33',
    status_list=[
        StatusList(
            id='id6',
            status='status8',
            reason='reason8'
        )
    ]
)
```

