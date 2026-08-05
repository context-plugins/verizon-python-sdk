
# Trigger Type 3

Trigger details.

## Structure

`TriggerType3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `str` | Optional | Trigger ID. |
| `trigger_name` | `str` | Optional | Trigger name. |
| `trigger_category` | `str` | Optional | This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be relevant when this parameter is set to this value. |
| `account_name` | `str` | Optional | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `anomaly_trigger_request` | [`AnomalyTriggerRequest`](../../doc/models/anomaly-trigger-request.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`TriggerNotification`](../../doc/models/trigger-notification.md) | Optional | The notification details of the trigger. |

## Example

```python
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.sms_number import SMSNumber
from verizon.models.trigger_notification import TriggerNotification
from verizon.models.trigger_type_3 import TriggerType3

trigger_type_3 = TriggerType3(
    trigger_id='595f5c44-c31c-4552-8670-020a1545a84d',
    trigger_name='Anomaly Daily Usage REST Test-Patch Update 4',
    trigger_category='UsageAnomaly',
    account_name='0000123456-00001',
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=False,
        include_over_expected_usage=True
    ),
    notification=TriggerNotification(
        notification_type='DailySummary',
        callback=True,
        email_notification=False,
        notification_group_name='Anomaly Test API',
        notification_frequency_factor=3,
        notification_frequency_interval='Hourly',
        external_email_recipients='placeholder@verizon.com',
        sms_notification=True,
        sms_numbers=[
            SMSNumber(
                carrier='US Cellular',
                number='9299280711'
            )
        ],
        reminder=True,
        severity='Critical'
    )
)
```

