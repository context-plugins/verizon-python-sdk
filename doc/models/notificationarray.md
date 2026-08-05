
# Notificationarray

## Structure

`Notificationarray`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_type` | `str` | Optional | - |
| `callback` | `bool` | Optional | - |
| `email_notification` | `bool` | Optional | - |
| `notification_group_name` | `str` | Optional | - |
| `notification_frequency_factor` | `int` | Optional | - |
| `notification_frequency_interval` | `str` | Optional | - |
| `external_email_recipients` | `str` | Optional | - |
| `sms_notification` | `bool` | Optional | - |
| `sms_numbers` | List[[cellphonenumber](../../doc/models/cellphonenumber.md)] \| None | Optional | This is List of a container for any-of cases. |
| `reminder` | `bool` | Optional | - |
| `severity` | `str` | Optional | - |

## Example

```python
from verizon.models.notificationarray import Notificationarray

notificationarray = Notificationarray(
    notification_type='PerEvent',
    callback=True,
    email_notification=False,
    notification_group_name='Notification Group Name (User defined)',
    notification_frequency_factor=3,
    notification_frequency_interval='Daily',
    external_email_recipients='Email addresses',
    sms_notification=True,
    reminder=True,
    severity='Notify'
)
```

