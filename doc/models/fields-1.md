
# Fields 1

## Structure

`Fields1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`SearchDeviceByPropertyFields`](../../doc/models/search-device-by-property-fields.md) | Optional | List of device sensors and their most recently reported values. |

## Example

```python
from verizon.models.acceleration import Acceleration
from verizon.models.fields_1 import Fields1
from verizon.models.search_device_by_property_fields import SearchDeviceByPropertyFields

fields_1 = Fields1(
    item=SearchDeviceByPropertyFields(
        acceleration=Acceleration(
            x='x6',
            y='y4',
            z='z6'
        ),
        battery='battery0',
        humidity='humidity4',
        light='light6',
        pressure='pressure2'
    )
)
```

