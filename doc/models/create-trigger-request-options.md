
# Create Trigger Request Options

## Structure

`CreateTriggerRequestOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Trigger name. |
| `trigger_category` | `str` | Optional | This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be relevant when this parameter is set to this value. |
| `account_name` | `str` | Optional | Account name.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `anomaly_trigger_request` | [`AnomalyTriggerRequest`](../../doc/models/anomaly-trigger-request.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`TriggerNotification`](../../doc/models/trigger-notification.md) | Optional | The notification details of the trigger. |
| `active` | `bool` | Optional | Indicates anomaly detection is active<br />True - Anomaly detection is active.<br />False - Anomaly detection is not active. |

## Example

```python
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.create_trigger_request_options import CreateTriggerRequestOptions
from verizon.models.sms_number import SMSNumber
from verizon.models.trigger_notification import TriggerNotification

create_trigger_request_options = CreateTriggerRequestOptions(
    name='Anomaly Daily Usage REST Test-Patch 1',
    trigger_category='UsageAnomaly',
    account_name='0000123456-00001',
    anomaly_trigger_request=AnomalyTriggerRequest(
        account_names='0000123456-00001',
        include_abnormal=True,
        include_very_abnormal=True,
        include_under_expected_usage=True,
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

