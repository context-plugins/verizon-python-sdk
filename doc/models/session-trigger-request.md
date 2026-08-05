
# Session Trigger Request

## Structure

`SessionTriggerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `comparator` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `threshold` | `int` | Optional | **Constraints**: `>= 0`, `<= 100` |

## Example

```python
from verizon.models.session_trigger_request import SessionTriggerRequest

session_trigger_request = SessionTriggerRequest(
    comparator='comparator4',
    threshold=80
)
```

