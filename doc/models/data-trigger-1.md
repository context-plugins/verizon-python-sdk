
# Data Trigger 1

## Structure

`DataTrigger1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_criteria` | [`AccountLevelFilter`](../../doc/models/account-level-filter.md) | Optional | - |
| `condition` | [conditionType](../../doc/models/condition-type-enum.md) \| [conditionObjectCall](../../doc/models/condition-object-call.md) \| None | Optional | This is a container for any-of cases. |
| `action` | [`AccountLevelActionEnum`](../../doc/models/account-level-action-enum.md) | Optional | The action taken when trigger conditions are met |
| `condition_type` | [`ConditionTypeEnum`](../../doc/models/condition-type-enum.md) | Optional | The condition type being monitored |
| `comparitor` | [`ComparitorEnum`](../../doc/models/comparitor-enum.md) | Optional | The boolean of the comparison. `gt` is Greater Than, `lt` is Less Than and `eq` is Equal To |
| `threshold` | `int` | Optional | The threshold value the trigger monitors for |
| `threshold_unit` | [`ThresholdUnitEnum`](../../doc/models/threshold-unit-enum.md) | Optional | The units of the threshold. This can be KB, Kilobits, MB, Megabits, or GB, Gigabits |
| `cycle_type` | [`RulesCycleTypeEnum`](../../doc/models/rules-cycle-type-enum.md) | Optional | The interval to monitor for the threshold. This can be Daily, Weekly or Monthly |
| `allowance_threshold` | [`AllowanceThreshold`](../../doc/models/allowance-threshold.md) | Optional | - |

## Example

```python
from verizon.models.account_level_action_enum import AccountLevelActionEnum
from verizon.models.account_level_filter import AccountLevelFilter
from verizon.models.accountnames import Accountnames
from verizon.models.comparitor_enum import ComparitorEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.data_trigger_1 import DataTrigger1
from verizon.models.rules_cycle_type_enum import RulesCycleTypeEnum
from verizon.models.threshold_unit_enum import ThresholdUnitEnum

data_trigger_1 = DataTrigger1(
    filter_criteria=AccountLevelFilter(
        separate_or_combined='separateOrCombined4',
        account_names=Accountnames(
            account_name_list=[
                'accountNameList7',
                'accountNameList8',
                'accountNameList9'
            ]
        )
    ),
    condition=ConditionTypeEnum.INDIVIDUAL,
    action=AccountLevelActionEnum.NOTIFY,
    condition_type=ConditionTypeEnum.AGING,
    comparitor=ComparitorEnum.GT,
    threshold=100,
    threshold_unit=ThresholdUnitEnum.KB,
    cycle_type=RulesCycleTypeEnum.DAILY
)
```

