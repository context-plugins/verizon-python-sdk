
# Trigger Notification

The notification details of the trigger.

## Structure

`TriggerNotification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_type` | `str` | Optional | The type of notification, i.e. 'DailySummary'. |
| `callback` | `bool` | Optional | Whether or not the notification should be sent via callback.<br />true<br />false. |
| `email_notification` | `bool` | Optional | Whether or not the notification should be sent via e-mail.<br />true<br />false. |
| `notification_group_name` | `str` | Optional | Name for the notification group. |
| `notification_frequency_factor` | `int` | Optional | Frequency factor for notification. |
| `notification_frequency_interval` | `str` | Optional | Frequency interval for notification. |
| `external_email_recipients` | `str` | Optional | E-mail address(es) where the notification should be delivered. |
| `sms_notification` | `bool` | Optional | SMS notification. |
| `sms_numbers` | [`List[SMSNumber]`](../../doc/models/sms-number.md) | Optional | List of SMS numbers.<br><br>**Constraints**: *Maximum Items*: `10` |
| `reminder` | `bool` | Optional | - |
| `severity` | `str` | Optional | Severity level associated with the notification. Examples would be:<br />Major<br />Minor<br />Critical<br />NotApplicable. |

## Example

```python
from verizon.models.sms_number import SMSNumber
from verizon.models.trigger_notification import TriggerNotification

trigger_notification = TriggerNotification(
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
```

