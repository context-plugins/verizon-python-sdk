
# Service Plan Update Request

Request to update service plan.

## Structure

`ServicePlanUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_plan` | `str` | Required | The service plan code that you want to assign to all specified devices. |
| `account_name` | `str` | Optional | The name of a billing account. |
| `current_service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | A list of the devices that you want to change, specified by device identifier. |
| `group_name` | `str` | Optional | The name of a device group, if you want to restore service for all devices in that group. |
| `carrier_ip_pool_name` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `take_effect` | `datetime` | Optional | - |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId
from verizon.models.service_plan_update_request import ServicePlanUpdateRequest

service_plan_update_request = ServicePlanUpdateRequest(
    service_plan='new_service_plan_code',
    account_name='accountName6',
    current_service_plan='currentServicePlan8',
    custom_fields=[
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
                    id='A100003685E561',
                    kind='meid'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    group_name='groupName8'
)
```

