
# Anomaly Trigger Result

A result containing a list of anomaly triggers.

## Structure

`AnomalyTriggerResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `triggers` | List[[AnomalyTriggerValue](../../doc/models/anomaly-trigger-value.md) \| [TriggerType2](../../doc/models/trigger-type-2.md)] \| None | Optional | Trigger value chunk details. |

## Example

```python
from verizon.models.anomaly_trigger_result import AnomalyTriggerResult
from verizon.models.anomaly_trigger_value import AnomalyTriggerValue
from verizon.models.notification_group_name_trigger_attribute import NotificationGroupNameTriggerAttribute

anomaly_trigger_result = AnomalyTriggerResult(
    triggers=[
        AnomalyTriggerValue(
            trigger_id='BE1B5958-3E11-41DB-9ABD-B1B7618C0035',
            trigger_name='Anomaly Daily Usage REST Test-1',
            organization_name='AnamolyDetectionRTRTest',
            trigger_category='UsageAnomaly',
            trigger_attributes=[
                NotificationGroupNameTriggerAttribute(
                    key='DataPercentage50'
                )
            ],
            created_at='2021-10-21T23:57:03.397.0000Z',
            modified_at='2021-10-21T23:57:03.397.0000Z'
        )
    ]
)
```

