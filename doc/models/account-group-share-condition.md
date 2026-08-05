
# Account Group Share Condition

## Structure

`AccountGroupShareCondition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`ConditionActionEnum`](../../doc/models/condition-action-enum.md) | Optional | The action taken when trigger conditions are met |

## Example

```python
from verizon.models.account_group_share_condition import AccountGroupShareCondition
from verizon.models.condition_action_enum import ConditionActionEnum

account_group_share_condition = AccountGroupShareCondition(
    action=ConditionActionEnum.NOTIFY
)
```

