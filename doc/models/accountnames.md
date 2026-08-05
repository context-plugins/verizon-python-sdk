
# Accountnames

## Structure

`Accountnames`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name_list` | `List[str]` | Optional | - |

## Example

```python
from verizon.models.accountnames import Accountnames

accountnames = Accountnames(
    account_name_list=[
        'accountNameList1',
        'accountNameList2',
        'accountNameList3'
    ]
)
```

