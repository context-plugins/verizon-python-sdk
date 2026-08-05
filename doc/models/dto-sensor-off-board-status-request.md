
# Dto Sensor Off Board Status Request

## Structure

`DtoSensorOffBoardStatusRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `gatewayidentifier` | [`Gatewayidentifier`](../../doc/models/gatewayidentifier.md) | Optional | - |
| `offboarding` | [`Offboarding`](../../doc/models/offboarding.md) | Optional | - |

## Example

```python
from verizon.models.dto_sensor_off_board_status_request import DtoSensorOffBoardStatusRequest
from verizon.models.gatewayidentifier import Gatewayidentifier
from verizon.models.offboarding import Offboarding

dto_sensor_off_board_status_request = DtoSensorOffBoardStatusRequest(
    accountname='0000123456-00001',
    gatewayidentifier=Gatewayidentifier(
        deviceid='deviceid0'
    ),
    offboarding=Offboarding(
        sensoridentifier='sensoridentifier8'
    )
)
```

