
# Account Service

Service associated with the account.

## Structure

`AccountService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the service plan. |
| `description` | `str` | Optional | The description of the service plan. |
| `states` | [`List[State]`](../../doc/models/state.md) | Optional | The state of the service plan. |

## Example

```python
from verizon.models.account_service import AccountService
from verizon.models.state import State

account_service = AccountService(
    name='Svc1',
    description='Usage Segmentation - Main Line.',
    states=[
        State(
            name='Svc1 Activate',
            workflow_sequence_number=1,
            service_plans=[
                '4523aef7250f67205fd5',
                '4d4090c0f2d48814c94d'
            ]
        ),
        State(
            name='Svc1 No Telematics',
            workflow_sequence_number=3,
            service_plans=[
                '4523aef7250f67205fd5',
                '4d4090c0f2d48814c94d'
            ]
        ),
        State(
            name='Svc1 Deactivate',
            workflow_sequence_number=2,
            service_plans=[
                '4523aef7250f67205fd5',
                '4d4090c0f2d48814c94d'
            ]
        )
    ]
)
```

