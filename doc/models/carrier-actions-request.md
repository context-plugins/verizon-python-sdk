
# Carrier Actions Request

Request for a carrier action.

## Structure

`CarrierActionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The name of a billing account. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | The devices for which you want to restore service, specified by device identifier. |
| `with_billing` | `bool` | Optional | set to "true" to suspend with billing, set to "false" to suspend without billing |
| `group_name` | `str` | Optional | The name of a device group, if you want to restore service for all devices in that group. |
| `service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.carrier_actions_request import CarrierActionsRequest
from verizon.models.device_id import DeviceId

carrier_actions_request = CarrierActionsRequest(
    account_name='accountName0',
    custom_fields=[
        None
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
    with_billing=False,
    group_name='groupName4'
)
```

