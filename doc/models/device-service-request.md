
# Device Service Request

Device information.

## Structure

`DeviceServiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Required | The International Mobile Equipment Identifier of the device. |
| `bullseye_enable` | [`HplBullseyeEnable`](../../doc/models/hpl-bullseye-enable.md) | Required | A flag that shows if Hyper Precise is enabled (true) or disabled (false). |

## Example

```python
from verizon.models.device_service_request import DeviceServiceRequest
from verizon.models.hpl_bullseye_enable import HplBullseyeEnable

device_service_request = DeviceServiceRequest(
    imei='15-digit IMEI',
    bullseye_enable=HplBullseyeEnable(
        bullseye_enable=True
    )
)
```

