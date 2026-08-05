
# Account Level Filter

## Structure

`AccountLevelFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `separate_or_combined` | `str` | Optional | Determines whether or not to aggregate usage of multiple accounts together, or separate by account. If this is null or not present, then the trigger will be for an individual line. |
| `account_names` | [`Accountnames`](../../doc/models/accountnames.md) | Optional | - |

## Example

```python
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.accountnames import Accountnames

account_level_filter = AccountLevelFilter(
    separate_or_combined='Separate',
    account_names=Accountnames(
        account_name_list=[
            'accountNameList7',
            'accountNameList8',
            'accountNameList9'
        ]
    )
)
```

