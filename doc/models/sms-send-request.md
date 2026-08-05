
# SMS Send Request

Request to send SMS.

## Structure

`SMSSendRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. |
| `sms_message` | `str` | Required | The contents of the SMS message. The SMS message is limited to 160 characters in 7-bit format, or 140 characters in 8-bit format. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The names and values of custom fields, if you want to only include devices that have matching custom fields. |
| `data_encoding` | `str` | Optional | The SMS message encoding, which can be 7-bit (default), 8-bit-ASCII, 8-bit-UTF-8, 8-bit-DATA. |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | The devices that you want to send the message to, specified by device identifier. |
| `group_name` | `str` | Optional | The name of a device group, if you want to send the SMS message to all devices in the device group. |
| `service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |
| `time_to_live` | `str` | Optional | A period of time the message remains valid or an end date for the message. This value would be less than the 5 day default. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId
from verizon.models.sms_send_request import SMSSendRequest

sms_send_request = SMSSendRequest(
    account_name='accountName8',
    sms_message='The rain in Spain stays mainly in the plain.',
    custom_fields=[
        CustomFields(
            key='key0',
            value='value2'
        )
    ],
    data_encoding='dataEncoding6',
    device_ids=[
        DeviceId(
            id='id0',
            kind='kind8'
        )
    ],
    group_name='groupName6',
    service_plan='T Plan 2'
)
```

