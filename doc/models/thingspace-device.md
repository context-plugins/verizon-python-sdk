
# Thingspace Device

Device that exist in Verizon Mobile Device Management (MDM).

## Structure

`ThingspaceDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | The billing account that the device is associated with. |
| `billing_cycle_end_date` | `str` | Optional | The date that the device's current billing cycle ends. |
| `carrier_informations` | [`List[CarrierInformation]`](../../doc/models/carrier-information.md) | Optional | The carrier information associated with the device. |
| `connected` | `bool` | Optional | True if the device is connected; false if it is not. |
| `created_at` | `str` | Optional | The date and time that the device was added to the system. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | The custom fields and values that have been set for the device. |
| `device_ids` | [`List[DeviceId]`](../../doc/models/device-id.md) | Optional | All identifiers for the device. |
| `extended_attributes` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | Any extended attributes for the device, as Key and Value pairs. The pairs listed below are returned as part of the response for a single device, but are not included if the request was for information about multiple devices. |
| `group_names` | `List[str]` | Optional | The device groups that the device belongs to. |
| `ipaddress` | `str` | Optional | The IP address of the device. |
| `last_activation_by` | `str` | Optional | The user who last activated the device. |
| `last_activation_date` | `str` | Optional | The date and time that the device was last activated. |
| `last_connection_date` | `str` | Optional | The most recent connection date and time. |

## Example

```python
from verizon.models.carrier_information import CarrierInformation
from verizon.models.device_id import DeviceId
from verizon.models.thingspace_device import ThingspaceDevice

thingspace_device = ThingspaceDevice(
    account_name='0000123456-00001',
    billing_cycle_end_date='2020-05-09T20:00:00-04:00',
    carrier_informations=[
        CarrierInformation(
            carrier_name='Verizon Wireless',
            service_plan='m2m4G',
            state='active'
        )
    ],
    connected=False,
    created_at='2019-08-07T10:42:15-04:00',
    device_ids=[
        DeviceId(
            id='10-digit MDN',
            kind='mdn'
        ),
        DeviceId(
            id='15-digit IMEI',
            kind='imei'
        )
    ],
    group_names=[
        'southwest'
    ],
    ipaddress='0.0.0.0',
    last_activation_by='Joe Q Public',
    last_activation_date='2019-08-07T10:42:34-04:00',
    last_connection_date='2020-03-12T04:23:37-04:00'
)
```

