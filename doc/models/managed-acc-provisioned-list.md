
# Managed Acc Provisioned List

## Structure

`ManagedAccProvisionedList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Account name |
| `txid` | `str` | Optional | Transaction identifier |

## Example

```python
from verizon.models.managed_acc_provisioned_list import ManagedAccProvisionedList

managed_acc_provisioned_list = ManagedAccProvisionedList(
    id='2334445555-00001',
    txid='d4fbff33-eeee-ffff-gggg-2c90bd287e3b'
)
```

