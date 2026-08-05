
# Trigger Type 2

Trigger details.

## Structure

`TriggerType2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `anomalyattributes` | [`UsageAnomalyAttributes`](../../doc/models/usage-anomaly-attributes.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`TriggerNotification`](../../doc/models/trigger-notification.md) | Optional | The notification details of the trigger. |

## Example

```python
from verizon.models.sms_number import SMSNumber
from verizon.models.trigger_notification import TriggerNotification
from verizon.models.trigger_type_2 import TriggerType2
from verizon.models.usage_anomaly_attributes import UsageAnomalyAttributes

trigger_type_2 = TriggerType2(
    anomalyattributes=UsageAnomalyAttributes(
        account_names='0000123456-00001',
        device_group='User Group 1',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
        include_over_expected_usage=True
    ),
    notification=TriggerNotification(
        notification_type='DailySummary',
        callback=True,
        email_notification=True,
        notification_group_name='Anomaly Test API',
        notification_frequency_factor=-2147483648,
        external_email_recipients='placeholder@verizon.com',
        sms_notification=True,
        sms_numbers=[
            SMSNumber(
                carrier='US Cellular',
                number='9299280711'
            )
        ],
        reminder=False,
        severity='Critical'
    )
)
```

