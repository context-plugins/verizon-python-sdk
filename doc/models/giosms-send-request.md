
# GIOSMS Send Request

## Structure

`GIOSMSSendRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | - |
| `custom_fields` | [`List[KvPair]`](../../doc/models/kv-pair.md) | Optional | **Constraints**: *Maximum Items*: `5` |
| `data_encoding` | `str` | Optional | - |
| `group_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `time_to_live` | `str` | Optional | A period of time the message remains valid or an end date for the message. This value would be less than the 5 day default. |
| `device_ids` | [`List[GIODeviceId]`](../../doc/models/gio-device-id.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `sms_message` | `str` | Required | - |

## Example

```python
from verizon.models.giosms_send_request import GIOSMSSendRequest
from verizon.models.kv_pair import KvPair

giosms_send_request = GIOSMSSendRequest(
    sms_message='A text message',
    account_name='accountName6',
    custom_fields=[
        KvPair(
            key='key0',
            value='value2'
        )
    ],
    data_encoding='dataEncoding4',
    group_name='groupName8',
    service_plan='servicePlan8'
)
```

