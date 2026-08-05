
# Device Prl List Request

Requests the current PRL (Preferred Roaming List) version for 2G or 3G devices, which can help determine which devices need a PRL update. (4G and GSM devices do not have a PRL.).

## Structure

`DevicePrlListRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | The devices for which you want the PRL version, specified by device identifier. You only need to provide one identifier per device. Do not use any of the other parameters if you specify device IDs. |
| `account_name` | `str` | Optional | The name of a billing account. This parameter is only required if you are passing groupName and the UWS account used for the current API session has access to multiple billing accounts, because the same device group name can exist in multiple accounts.An account name is usually numeric, and must include any leading zeros. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The names and values of custom fields, if you want to only include devices that have matching custom fields. |
| `group_name` | `str` | Optional | The name of a device group, if you want to only include devices in that group. |
| `service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId
from verizon.models.device_prl_list_request import DevicePrlListRequest

device_prl_list_request = DevicePrlListRequest(
    device_ids=[
        DeviceId(
            id='id0',
            kind='kind8'
        ),
        DeviceId(
            id='id0',
            kind='kind8'
        ),
        DeviceId(
            id='id0',
            kind='kind8'
        )
    ],
    account_name='101234-0001',
    custom_fields=[
        CustomFields(
            key='key0',
            value='value2'
        ),
        CustomFields(
            key='key0',
            value='value2'
        ),
        CustomFields(
            key='key0',
            value='value2'
        )
    ],
    group_name='West Region',
    service_plan='3G 2MB'
)
```

