
# Bullseye Service Request

Account number and list of devices.

## Structure

`BullseyeServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | [`List[DeviceServiceRequest]`](../../doc/models/device-service-request.md) | Required | A list of devices. |
| `account_number` | `str` | Required | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |

## Example

```python
from verizon.models.bullseye_service_request import BullseyeServiceRequest
from verizon.models.device_service_request import DeviceServiceRequest
from verizon.models.hpl_bullseye_enable import HplBullseyeEnable

bullseye_service_request = BullseyeServiceRequest(
    device_list=[
        DeviceServiceRequest(
            imei='15-digit IMEI',
            bullseye_enable=HplBullseyeEnable(
                bullseye_enable=True
            )
        )
    ],
    account_number='0000123456-00001'
)
```

