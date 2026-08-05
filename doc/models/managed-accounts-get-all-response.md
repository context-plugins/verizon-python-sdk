
# Managed Accounts Get All Response

## Structure

`ManagedAccountsGetAllResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account Name |
| `managed_acc_added_list` | [`List[ManagedAccAddedList]`](../../doc/models/managed-acc-added-list.md) | Optional | - |
| `managed_acc_provisioned_list` | [`List[ManagedAccProvisionedList]`](../../doc/models/managed-acc-provisioned-list.md) | Optional | - |

## Example

```python
from verizon.models.managed_acc_added_list import ManagedAccAddedList
from verizon.models.managed_acc_provisioned_list import ManagedAccProvisionedList
from verizon.models.managed_accounts_get_all_response import ManagedAccountsGetAllResponse

managed_accounts_get_all_response = ManagedAccountsGetAllResponse(
    account_name='0212312345-00001',
    managed_acc_added_list=[
        ManagedAccAddedList(
            id='id6',
            txid='txid6'
        ),
        ManagedAccAddedList(
            id='id6',
            txid='txid6'
        )
    ],
    managed_acc_provisioned_list=[
        ManagedAccProvisionedList(
            id='id2',
            txid='txid0'
        ),
        ManagedAccProvisionedList(
            id='id2',
            txid='txid0'
        )
    ]
)
```

