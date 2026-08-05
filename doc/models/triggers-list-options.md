
# Triggers List Options

## Structure

`TriggersListOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | The system assigned name of the trigger being updated. |
| `trigger_name` | `str` | Optional | The user defined name of the trigger. |
| `organization_name` | `str` | Optional | The user assigned name of the organization associated with the trigger. |
| `trigger_category` | `str` | Optional | This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be relevant when this parameter is set to this value. |
| `trigger_attributes` | List[[NotificationGroupNameTriggerAttribute](../../doc/models/notification-group-name-trigger-attribute.md) \| [ServicePlanTriggerAttribute](../../doc/models/service-plan-trigger-attribute.md) \| [DataPercentage50TriggerAttribute](../../doc/models/data-percentage-50-trigger-attribute.md) \| [DataPercentage75TriggerAttribute](../../doc/models/data-percentage-75-trigger-attribute.md) \| [DataPercentage90TriggerAttribute](../../doc/models/data-percentage-90-trigger-attribute.md) \| [DataPercentage100TriggerAttribute](../../doc/models/data-percentage-100-trigger-attribute.md)] \| None | Optional | Additional details and keys for the trigger. |
| `created_at` | `str` | Optional | Timestamp for whe the trigger was created. |
| `modified_at` | `str` | Optional | Timestamp for the most recent time the trigger was modified. |
| `anomalyattributes` | [`UsageAnomalyAttributes`](../../doc/models/usage-anomaly-attributes.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`TriggerNotification`](../../doc/models/trigger-notification.md) | Optional | The notification details of the trigger. |

## Example

```python
from verizon.models.notification_group_name_trigger_attribute import NotificationGroupNameTriggerAttribute
from verizon.models.triggers_list_options import TriggersListOptions

triggers_list_options = TriggersListOptions(
    trigger_id='BE1B5958-3E11-41DB-9ABD-B1B7618C0035',
    trigger_name='Anomaly Daily Usage REST Test-1',
    organization_name='AnamolyDetectionRTRTest',
    trigger_category='UsageAnomaly',
    trigger_attributes=[
        NotificationGroupNameTriggerAttribute(
            key='DataPercentage50'
        )
    ],
    created_at='2021-10-21T23:57:03.397Z',
    modified_at='2021-10-21T23:57:03.397Z'
)
```

