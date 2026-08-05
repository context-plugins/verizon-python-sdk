
# Gatewayidentifier

## Structure

`Gatewayidentifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deviceid` | `str` | Optional | a unique parent deviceid used to group all Lora sensors. Sensors need parent gateway for connection |

## Example

```python
from verizon.models.gatewayidentifier import Gatewayidentifier

gatewayidentifier = Gatewayidentifier(
    deviceid='UUID of the Gateway device'
)
```

