
# Data Trigger Request

## Structure

`DataTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `comparator` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `threshold` | `int` | Optional | **Constraints**: `>= 0`, `<= 100` |
| `threshold_unit` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.data_trigger_request import DataTriggerRequest

data_trigger_request = DataTriggerRequest(
    comparator='comparator6',
    threshold=100,
    threshold_unit='thresholdUnit2'
)
```

