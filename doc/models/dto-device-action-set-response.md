
# Dto Device Action Set Response

## Structure

`DtoDeviceActionSetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `actionresult` | [`List[ActionResultwithDeviceConfig]`](../../doc/models/action-resultwith-device-config.md) | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.action_resultwith_device_config import ActionResultwithDeviceConfig
from verizon.models.dto_device_action_set_configuration import DtoDeviceActionSetConfiguration
from verizon.models.dto_device_action_set_response import DtoDeviceActionSetResponse
from verizon.models.dto_device_config import DtoDeviceConfig
from verizon.models.sensor_insights_ble import SensorInsightsBLE

dto_device_action_set_response = DtoDeviceActionSetResponse(
    actionresult=[
        ActionResultwithDeviceConfig(
            createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            description='description8',
            deviceid='deviceid8',
            errmsg='errmsg0',
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
            )
        ),
        ActionResultwithDeviceConfig(
            createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            description='description8',
            deviceid='deviceid8',
            errmsg='errmsg0',
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
            )
        ),
        ActionResultwithDeviceConfig(
            createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            description='description8',
            deviceid='deviceid8',
            errmsg='errmsg0',
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
            )
        )
    ]
)
```

