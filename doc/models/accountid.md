
# Accountid

## Structure

`Accountid`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The numeric name of the account and must include leading zeroes |
| `mtas_account_number` | `str` | Optional | - |

## Example

```python
from verizon.models.accountid import Accountid

accountid = Accountid(
    account_name='0000123456-00001',
    mtas_account_number='0000123456-00001'
)
```

