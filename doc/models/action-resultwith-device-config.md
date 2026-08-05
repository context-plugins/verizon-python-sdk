
# Action Resultwith Device Config

## Structure

`ActionResultwithDeviceConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `createdon` | `datetime` | Optional | Timestamp of the record |
| `description` | `str` | Optional | - |
| `deviceid` | `str` | Optional | This is a UUID value of the device created when the device is onboarded |
| `errmsg` | `str` | Optional | Error message |
| `fields` | [`DtoDeviceActionSetConfiguration`](../../doc/models/dto-device-action-set-configuration.md) | Optional | - |
| `foreignid` | `str` | Optional | UUID of the ECPD account the user belongs to |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `lastupdated` | `datetime` | Optional | Timestamp of the record |
| `state` | `str` | Optional | The current status of the device or transaction and will be `success` or `failed` |
| `transactionid` | `str` | Optional | The system-generated UUID of the transaction |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Optional | The UUID of the resource version |

## Example

```python
import dateutil.parser

from verizon.models.action_resultwith_device_config import ActionResultwithDeviceConfig
from verizon.models.dto_device_action_set_configuration import DtoDeviceActionSetConfiguration
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.sensor_insights_ble import SensorInsightsBLE

action_resultwith_device_config = ActionResultwithDeviceConfig(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    description='description6',
    deviceid='The UUID of the device',
    errmsg='provider_service_error',
    fields=DtoDeviceActionSetConfiguration(
        device_config=DtoDeviceConfig(
            ble=SensorInsightsBLE(
                data_mode=216,
                manufacturer_id=180,
                max_num_scan=126,
                min_sig_str=60,
                monitor_period=88
            )
        )
    ),
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    state='success',
    transactionid='afbcc00d-eeee-ffff-gggg-38b4333fcf06',
    version='1.0',
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395'
)
```

