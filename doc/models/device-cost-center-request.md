
# Device Cost Center Request

Request to retrieve cost center value of a device.

## Structure

`DeviceCostCenterRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of a billing account. |
| `cost_center` | `str` | Optional | The new cost center code. Valid values are any string of up to 36 alphanumeric characters, space, dash, exclamation point, and pound sign. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | A list of the devices that you want to change, specified by device identifier. Do not include accountName, groupName, customFields, or servicePlan if you use this parameter. |
| `group_name` | `str` | Optional | The name of a device group, if you want to only include devices in that group. |
| `primary_place_of_use` | `Any` | Optional | The customer name and the address of the device's primary place of use. These values are applied to all devices in the request.The Primary Place of Use location may affect taxation or have other legal implications. You may want to speak with legal and/or financial advisers before entering values for these fields. |
| `remove_cost_center` | `bool` | Optional | Set to true to remove the cost center code value. This flag takes precedence over a new costCenter value. If this flag is true and costCenter has a value, the cost center code is removed. Do not include this parameter, or set it to false to change the costCenter value. |
| `service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields
from verizon.models.device_cost_center_request import DeviceCostCenterRequest
from verizon.models.device_id import DeviceId

device_cost_center_request = DeviceCostCenterRequest(
    account_name='accountName6',
    cost_center='cc12345',
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
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='89148000000800139708',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    group_name='groupName8'
)
```

