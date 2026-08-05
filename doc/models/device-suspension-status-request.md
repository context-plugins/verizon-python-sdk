
# Device Suspension Status Request

Request to return service suspension information about one or more devices.

## Structure

`DeviceSuspensionStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | The devices that you want to include in the request, specified by device identifier. You only need to provide one identifier per device. |
| `filter` | [`DeviceFilterWithoutAccount`](../../doc/models/device-filter-without-account.md) | Optional | Filter for devices without account. |
| `account_name` | `str` | Optional | The name of a billing account. |

## Example

```python
from verizon.models.custom_fields import CustomFields
from verizon.models.device_filter_without_account import DeviceFilterWithoutAccount
from verizon.models.device_id import DeviceId
from verizon.models.device_suspension_status_request import DeviceSuspensionStatusRequest

device_suspension_status_request = DeviceSuspensionStatusRequest(
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
    filter=DeviceFilterWithoutAccount(
        group_name='suspended devices',
        service_plan='servicePlan6',
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
        ]
    ),
    account_name='1223334444-00001'
)
```

