
# Engagement

The engagements associated with the account.

## Structure

`Engagement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `engagement_id` | `str` | Optional | The engagement ID. |
| `charging_group` | `str` | Optional | The charging group name. |
| `services` | [`List[AccountService]`](../../doc/models/account-service.md) | Optional | The services associated with the account. |

## Example

```python
from verizon.models.account_service import AccountService
from verizon.models.engagement import Engagement
from verizon.models.state import State

engagement = Engagement(
    engagement_id='1234',
    charging_group='Engagement1234',
    services=[
        AccountService(
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
        ),
        AccountService(
            name='WIFI',
            description='Usage Segmentation - WiFi.',
            states=[
                State(
                    name='WIFI Redirect',
                    workflow_sequence_number=2,
                    service_plans=[
                        '4d4090c0f2d48814c94d'
                    ]
                ),
                State(
                    name='WIFI Trial',
                    workflow_sequence_number=4,
                    service_plans=[
                        '4d4090c0f2d48814c94d'
                    ]
                ),
                State(
                    name='WIFI Goodwill',
                    workflow_sequence_number=6,
                    service_plans=[
                        '4d4090c0f2d48814c94d'
                    ]
                ),
                State(
                    name='WIFI Disable',
                    workflow_sequence_number=3,
                    service_plans=[
                        '4d4090c0f2d48814c94d'
                    ]
                )
            ]
        )
    ]
)
```

