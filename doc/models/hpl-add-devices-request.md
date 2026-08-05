
# Hpl Add Devices Request

Request to add the devices.

## Structure

`HplAddDevicesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `str` | Optional | The initial service state for the devices. The only valid state is "Preactive." |
| `devices_to_add` | [`List[HplAccountDeviceList]`](../../doc/models/hpl-account-device-list.md) | Optional | The devices that you want to add. |
| `account_name` | `str` | Optional | The numeric name of the account and must include leading zeroes. |
| `custom_fields` | [`List[HplCustomFields]`](../../doc/models/hpl-custom-fields.md) | Optional | The names and values for any custom fields that you want set for the devices as they are added to the account. |
| `group_name` | `str` | Optional | The name of a device group to add the devices to. They are added to the default device group if you don't include this parameter. |
| `sku_number` | `str` | Optional | The Stock Keeping Unit (SKU) number of a 4G device type with an embedded SIM. |
| `smsr_oid` | `str` | Optional | The Subscription Manager Secure Router Object ID, used for remote SIM provisioning. SMSR securely routes the download and management of eSIM profiles. |
| `number_of_virtual_imei` | `int` | Optional | numberOfVirtualImei. |
| `upload_type` | `str` | Optional | uploadType. |

## Example

```python
from verizon.models.hpl_account_device_list import HplAccountDeviceList
from verizon.models.hpl_add_devices_request import HplAddDevicesRequest
from verizon.models.hpl_custom_fields import HplCustomFields
from verizon.models.hpl_device_id import HplDeviceId

hpl_add_devices_request = HplAddDevicesRequest(
    state='preactive',
    devices_to_add=[
        HplAccountDeviceList(
            device_ids=[
                HplDeviceId(
                    kind='imei',
                    id='15-digit IMEI'
                ),
                HplDeviceId(
                    kind='iccid',
                    id='20-digit ICCID'
                )
            ]
        ),
        HplAccountDeviceList(
            device_ids=[
                HplDeviceId(
                    kind='imei',
                    id='15-digit IMEI'
                ),
                HplDeviceId(
                    kind='iccid',
                    id='20-digit ICCID'
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    custom_fields=[
        HplCustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='West Region',
    number_of_virtual_imei=1
)
```

