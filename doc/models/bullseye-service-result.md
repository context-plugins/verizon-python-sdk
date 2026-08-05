
# Bullseye Service Result

Status of Hyper Precise Location on the device.

## Structure

`BullseyeServiceResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Optional | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |
| `device_list` | [`List[DeviceServiceInformation]`](../../doc/models/device-service-information.md) | Optional | List of devices. |
| `response_type` | [`ApiResponseCode`](../../doc/models/api-response-code.md) | Optional | ResponseCode and/or a message indicating success or failure of the request. |

## Example

```python
from verizon.models.api_response_code import ApiResponseCode
from verizon.models.bullseye_service_result import BullseyeServiceResult
from verizon.models.device_service_information import DeviceServiceInformation
from verizon.models.hpl_bullseye_enable import HplBullseyeEnable
from verizon.models.response_code_enum import ResponseCodeEnum

bullseye_service_result = BullseyeServiceResult(
    account_number='0000123456-00001',
    device_list=[
        DeviceServiceInformation(
            imei='imei4',
            bullseye_enable=HplBullseyeEnable(
                bullseye_enable=False
            ),
            response_type=ApiResponseCode(
                response_code=ResponseCodeEnum.INTERNAL_ERROR,
                message='message8'
            )
        ),
        DeviceServiceInformation(
            imei='imei4',
            bullseye_enable=HplBullseyeEnable(
                bullseye_enable=False
            ),
            response_type=ApiResponseCode(
                response_code=ResponseCodeEnum.INTERNAL_ERROR,
                message='message8'
            )
        ),
        DeviceServiceInformation(
            imei='imei4',
            bullseye_enable=HplBullseyeEnable(
                bullseye_enable=False
            ),
            response_type=ApiResponseCode(
                response_code=ResponseCodeEnum.INTERNAL_ERROR,
                message='message8'
            )
        )
    ],
    response_type=ApiResponseCode(
        response_code=ResponseCodeEnum.INTERNAL_ERROR,
        message='message8'
    )
)
```

