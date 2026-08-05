
# Account Device List Result

Response for a request to list down account devices.

## Structure

`AccountDeviceListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[ThingspaceDevice]`](../../doc/models/thingspace-device.md) | Optional | Up to 10,000 devices that you want to move to a different account, specified by device identifier. |
| `has_more_data` | `bool` | Optional | False for a status 200 response.True for a status 202 response, indicating that there is more data to be retrieved. |

## Example

```python
from verizon.models.account_device_list_result import AccountDeviceListResult
from verizon.models.carrier_information import CarrierInformation
from verizon.models.device_id import DeviceId
from verizon.models.thingspace_device import ThingspaceDevice

account_device_list_result = AccountDeviceListResult(
    devices=[
        ThingspaceDevice(
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
    ],
    has_more_data=False
)
```

