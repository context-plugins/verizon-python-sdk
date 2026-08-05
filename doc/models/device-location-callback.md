
# Device Location Callback

## Structure

`DeviceLocationCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`CallbackServiceNameEnum`](../../doc/models/callback-service-name-enum.md) | Required | The name of the callback service. |
| `url` | `str` | Required | The location of your callback listener. |

## Example

```python
from verizon.models.callback_service_name_enum import CallbackServiceNameEnum
from verizon.models.device_location_callback import DeviceLocationCallback

device_location_callback = DeviceLocationCallback(
    name=CallbackServiceNameEnum.LOCATION,
    url='http://10.120.102.183:50559/CallbackListener/LocationServiceMessages.asmx'
)
```

