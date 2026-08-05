
# Move Device Request

Request to move active devices from one billing account to another within a customer profile.

## Structure

`MoveDeviceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of the billing account that you want to move the devices to. |
| `filter` | [`DeviceFilter`](../../doc/models/device-filter.md) | Optional | Specify the kind of the device identifier, the type of match, and the string that you want to match. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | Up to 10,000 devices that you want to move to a different account, specified by device identifier. |
| `group_name` | `str` | Optional | The name of a device group, to only include devices in that group. |
| `carrier_ip_pool_name` | `str` | Optional | The pool from which device IP addresses will be derived in the new account. If you do not include this element, the default pool will be used. |
| `service_plan` | `str` | Optional | The service plan code that you want to assign to the devices in the new account. If you do not include this element, ThingSpace will attempt to use the current service plan, which will result in a error if the new account does not have that service plan. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields
from verizon.models.device_filter import DeviceFilter
from verizon.models.move_device_request import MoveDeviceRequest

move_device_request = MoveDeviceRequest(
    account_name='0212345678-00001',
    filter=DeviceFilter(
        account='account4',
        group_name='Short-Haul Trucks',
        service_plan='servicePlan6',
        custom_fields=[
            CustomFields(
                key='CustomField1',
                value='East Region Trucks'
            )
        ]
    ),
    custom_fields=[
        None,
        CustomFields(
            key=None,
            value=None
        ),
        CustomFields(
            key=None,
            value=None
        )
    ],
    devices=[
        None,
        AccountDeviceList(
            device_ids=[]
        )
    ],
    group_name='groupName4',
    carrier_ip_pool_name='carrierIpPoolName2',
    service_plan='M2M5GB'
)
```

