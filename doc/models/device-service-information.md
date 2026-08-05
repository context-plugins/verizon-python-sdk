
# Device Service Information

Device service information.

## Structure

`DeviceServiceInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_type` | [`ApiResponseCode`](../../doc/models/api-response-code.md) | Optional | ResponseCode and/or a message indicating success or failure of the request. |
| `imei` | `str` | Required | The International Mobile Equipment Identifier of the device. |
| `bullseye_enable` | [`HplBullseyeEnable`](../../doc/models/hpl-bullseye-enable.md) | Required | A flag that shows if Hyper Precise is enabled (true) or disabled (false). |

## Example

```python
from verizon.models.api_response_code import ApiResponseCode
from verizon.models.device_service_information import DeviceServiceInformation
from verizon.models.hpl_bullseye_enable import HplBullseyeEnable
from verizon.models.response_code_enum import ResponseCodeEnum

device_service_information = DeviceServiceInformation(
    imei='15-digit IMEI',
    bullseye_enable=HplBullseyeEnable(
        bullseye_enable=True
    ),
    response_type=ApiResponseCode(
        response_code=ResponseCodeEnum.INTERNAL_ERROR,
        message='message8'
    )
)
```

