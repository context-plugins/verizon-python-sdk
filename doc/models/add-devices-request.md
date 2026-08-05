
# Add Devices Request

Request to add the devices.

## Structure

`AddDevicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `str` | Required | The initial service state for the devices. The only valid state is “Pre-active.” |
| `devices_to_add` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | The devices that you want to add. |
| `account_name` | `str` | Optional | The billing account to which the devices are added. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The names and values for any custom fields that you want set for the devices as they are added to the account. |
| `group_name` | `str` | Optional | The name of a device group to add the devices to. They are added to the default device group if you don't include this parameter. |
| `sku_number` | `str` | Optional | The Stock Keeping Unit (SKU) number of a 4G device type with an embedded SIM. |
| `smsr_oid` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.add_devices_request import AddDevicesRequest
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId

add_devices_request = AddDevicesRequest(
    state='Pre-active',
    devices_to_add=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='15-digit IMEI',
                    kind='imei'
                ),
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress2'
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='15-digit IMEI',
                    kind='imei'
                ),
                DeviceId(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress2'
        )
    ],
    account_name='0000123456-00001',
    custom_fields=[
        CustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='West Region',
    sku_number='skuNumber4',
    smsr_oid='smsrOid8'
)
```

