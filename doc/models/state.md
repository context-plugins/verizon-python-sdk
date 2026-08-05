
# State

Each service includes custom states.

## Structure

`State`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the state. |
| `workflow_sequence_number` | `float` | Optional | The workflow sequence number of this state. |
| `service_plans` | `List[str]` | Optional | The service plans that can be used to charge for services for devices in this state. |

## Example

```python
from verizon.models.state import State

state = State(
    name='Svc1 Activate',
    workflow_sequence_number=1,
    service_plans=[
        '4523aef7250f67205fd5',
        '4d4090c0f2d48814c94d'
    ]
)
```

