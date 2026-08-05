
# Rateplantype 2 Condition

## Structure

`Rateplantype2Condition`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `condition_type` | [`ConditionTypeEnum`](../../doc/models/condition-type-enum.md) | Optional | The condition type being monitored |
| `comparitor` | [`ComparitorEnum`](../../doc/models/comparitor-enum.md) | Optional | The boolean of the comparison. `gt` is Greater Than, `lt` is Less Than and `eq` is Equal To |
| `threshold` | `int` | Optional | The threshold value the trigger monitors for |
| `threshold_unit` | [`ThresholdUnitEnum`](../../doc/models/threshold-unit-enum.md) | Optional | The units of the threshold. This can be KB, Kilobits, MB, Megabits, or GB, Gigabits |
| `cycle_type` | [`RulesCycleTypeEnum`](../../doc/models/rules-cycle-type-enum.md) | Optional | The interval to monitor for the threshold. This can be Daily, Weekly or Monthly |
| `allowance_threshold` | [`AllowanceThreshold`](../../doc/models/allowance-threshold.md) | Optional | - |

## Example

```python
from verizon.models.comparitor_enum import ComparitorEnum
from verizon.models.condition_type_enum import ConditionTypeEnum
from verizon.models.rateplantype_2_condition import Rateplantype2Condition
from verizon.models.rules_cycle_type_enum import RulesCycleTypeEnum
from verizon.models.threshold_unit_enum import ThresholdUnitEnum

rateplantype_2_condition = Rateplantype2Condition(
    condition_type=ConditionTypeEnum.AGING,
    comparitor=ComparitorEnum.GT,
    threshold=100,
    threshold_unit=ThresholdUnitEnum.KB,
    cycle_type=RulesCycleTypeEnum.DAILY
)
```

