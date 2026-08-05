
# Suspenddetailsobject

## Structure

`Suspenddetailsobject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `suspend_from_accounts` | `List[str]` | Optional | - |
| `suspend_duration` | `int` | Optional | - |
| `suspend_option` | `str` | Optional | - |
| `threshold` | `int` | Optional | The threshold value the trigger monitors for |
| `threshold_unit` | [`ThresholdUnitEnum`](../../doc/models/threshold-unit-enum.md) | Optional | The units of the threshold. This can be KB, Kilobits, MB, Megabits, or GB, Gigabits |

## Example

```python
from verizon.models.suspenddetailsobject import Suspenddetailsobject
from verizon.models.threshold_unit_enum import ThresholdUnitEnum

suspenddetailsobject = Suspenddetailsobject(
    suspend_from_accounts=[
        'suspendFromAccounts7',
        'suspendFromAccounts8',
        'suspendFromAccounts9'
    ],
    suspend_duration=90,
    suspend_option='withBilling',
    threshold=100,
    threshold_unit=ThresholdUnitEnum.KB
)
```

