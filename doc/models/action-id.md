
# Action Id

## Structure

`ActionId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `originating_station_id` | `int` | Required | Unique ID for originating station. |
| `sequence_number` | `int` | Required | Counter used to differenciate multiple DENMs from same station. |

## Example

```python
from verizon.models.action_id import ActionId

action_id = ActionId(
    originating_station_id=46,
    sequence_number=24
)
```

