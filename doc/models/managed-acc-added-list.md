
# Managed Acc Added List

## Structure

`ManagedAccAddedList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | Account name |
| `txid` | `str` | Optional | Transaction identifier |

## Example

```python
from verizon.models.managed_acc_added_list import ManagedAccAddedList

managed_acc_added_list = ManagedAccAddedList(
    id='1223334444-00001',
    txid='2c90bd28-eeee-ffff-gggg-7e3bd4fbff33'
)
```

