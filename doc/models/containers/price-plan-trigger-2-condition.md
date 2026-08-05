
# Price Plan Trigger 2 Condition

## Data Type

`ConditionTypeEnum | ConditionObjectCall`

## Cases

| Type |
|  --- |
| [`ConditionTypeEnum`](../../../doc/models/condition-type-enum.md) |
| [`ConditionObjectCall`](../../../doc/models/condition-object-call.md) |

## ConditionTypeEnum

### Initialization Code

#### Example

```python
value = ConditionTypeEnum.AGING
```

## ConditionObjectCall

### Initialization Code

#### Example

```python
value = ConditionObjectCall(
    condition_type=ConditionTypeEnum.AGING,
    comparitor=ComparitorEnum.GT,
    threshold=100,
    threshold_unit=ThresholdUnitEnum.KB,
    cycle_type=RulesCycleTypeEnum.DAILY
)
```

