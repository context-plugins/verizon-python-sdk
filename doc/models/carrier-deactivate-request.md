
# Carrier Deactivate Request

Request to deactivate a carrier.

## Structure

`CarrierDeactivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | The name of a billing account. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | The devices for which you want to deactivate service, specified by device identifier. |
| `reason_code` | `str` | Required | Code identifying the reason for the deactivation. Currently the only valid reason code is “FF”, which corresponds to General Admin/Maintenance. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |
| `etf_waiver` | `bool` | Optional | Fees may be assessed for deactivating Verizon Wireless devices, depending on the account contract. The etfWaiver parameter waives the Early Termination Fee (ETF), if applicable. |
| `group_name` | `str` | Optional | The name of a device group, if you want to deactivate all devices in that group. |
| `service_plan` | `str` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |
| `delete_after_deactivation` | `bool` | Optional | - |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.carrier_deactivate_request import CarrierDeactivateRequest
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId

carrier_deactivate_request = CarrierDeactivateRequest(
    account_name='0000123456-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress4'
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    reason_code='FF',
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
    etf_waiver=True,
    group_name='groupName0',
    service_plan='servicePlan0',
    delete_after_deactivation=False
)
```

