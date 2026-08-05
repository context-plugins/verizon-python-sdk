
# Dto Sensor on Board Status Request

## Structure

`DtoSensorOnBoardStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `gatewayidentifier` | [`Gatewayidentifier`](../../doc/models/gatewayidentifier.md) | Optional | - |
| `onboarding` | [`Onboarding`](../../doc/models/onboarding.md) | Optional | - |

## Example

```python
from verizon.models.dto_sensor_on_board_status_request import DtoSensorOnBoardStatusRequest
from verizon.models.gatewayidentifier import Gatewayidentifier
from verizon.models.onboarding import Onboarding

dto_sensor_on_board_status_request = DtoSensorOnBoardStatusRequest(
    accountname='0000123456-00001',
    gatewayidentifier=Gatewayidentifier(
        deviceid='deviceid0'
    ),
    onboarding=Onboarding(
        sensoridentifier='sensoridentifier4'
    )
)
```

